from django.core.exceptions import ValidationError
from django.db import models
import requests
import logging

logger = logging.getLogger(__name__)


class Interval(models.Model):
    INTERVALS = (
        (0, '10 sec'),
        (1, '30 sec'),
        (2, '60 sec')
    )
    value = models.IntegerField(default=0, null=True, choices=INTERVALS)

    def save(self, *args, **kwargs):
        if not self.pk and Interval.objects.exists():
            raise ValidationError('There is can be only one instance')
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.get_value_display()}'

    @staticmethod
    def get_milliseconds():
        if Interval.objects.first():
            seconds = int(Interval.objects.first().get_value_display()[:2])
            return seconds * 1000
        return 10 * 1000


class Link(models.Model):
    url = models.URLField(unique=True, null=True)
    pause = models.BooleanField(default=False)

    @property
    def interval(self):
        return Interval.objects.first()

    def __str__(self):
        return f'{self.url} pause:{self.pause}'

    @staticmethod
    def check_statuses():
        """
        return array of urls with not 200
        """
        result = []
        for status in Link.objects.filter(pause=False):
            try:
                request = requests.get(status.url)
                if request.status_code != 200:
                    result.append(status.url)

            except requests.exceptions.HTTPError as err:
                logger.error(err)

        return result
