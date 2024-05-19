## change .env file

## python manage.py inspectdb > customadmin/models.py


-- copy customadmin/models.py file and remove customadmin/models.py file
-- create customadmin/models.py and paste customadmin/models.py


```
python manage.py makemigrations customadmin
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
