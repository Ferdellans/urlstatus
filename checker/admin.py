from django.utils.html import mark_safe
from django.contrib import admin
from .models import Link, Interval


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'blank_url', 'pause', 'interval')
    list_filter = ('pause',)
    list_search = ('url',)

    def blank_url(self, obj):
        return mark_safe(f'<a href="{obj.url}" target="_blank">{obj.url}</a>')


@admin.register(Interval)
class IntervalAdmin(admin.ModelAdmin):
    list_display = ('id', 'value')
