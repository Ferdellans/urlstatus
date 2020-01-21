test url status checker

Python 3.6

1. venv env
2. source /env/bin/activate
3. mkdir urlstatus
4. cd urlstatus
5. git clone https://github.com/Ferdellans/urlstatus.git
6. pip install -r requirements.txt
7. python manage.py makemigrations
8. python manage.py makemigrations checker
9. python manage.py migrate
10. python manage.py createsuperuser
11. python manage.py runserver
12. open http://127.0.0.1:8000/admin
13. login as superuser
14. Create interval
15. Create Links as much as you wish
16. open http://127.0.0.1:8000/

js will initialize setEventTimer for refresh url function every for check interval, that ou have to add into django ORM

# todo
1. celery app
2. celery worker for checking urls
3. celery schedule in django settings
4. broker (redis/rabbtimq) for celery worker
5. (optional) if not used django shedule celery - create supervithor for celery worker
6. remove js script from index
