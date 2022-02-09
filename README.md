# OnlinePythonCompiler #

## Python Compiler API /python ##

1 - Setting up a virtual environment 

Create a virtual environment
```
...\> py -m venv project-name
```
Activate the environment
```
...\> project-name\Scripts\activate.bat
```

2 - Install package

> asgiref==3.4.1___backports.zoneinfo==0.2.1
dj-database-url==0.5.0
dj-static==0.0.6
Django==4.0.1
django-heroku==0.3.1
django-toolbelt==0.0.1
djangorestframework==3.13.1
gunicorn==20.1.0
psycopg2==2.9.3
pytz==2021.3
sqlparse==0.4.2
static3==0.7.0
tzdata==2021.5
whitenoise==5.3.0



heroku git:remote -a pythoncompiler9

git remote show heroku

git push heroku master

git remote add origin  https://github.com/lykienminh/OnlinePythonCompiler.git

..\Scripts\activate

1 - heroku config:set DISABLE_COLLECTSTATIC=1 // Not sure if this was necessary eventually as I guess problem with collect static was due to no module found error.

2 - pip freeze > requirements.txt // to make sure rest_framework is included in the file.

3 - then proceeding with the git push.

4 - heroku config:set DISABLE_COLLECTSTATIC

5 - heroku run python manage.py collectstatic