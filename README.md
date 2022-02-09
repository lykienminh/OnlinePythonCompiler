# OnlinePythonCompiler #

## Python Compiler API /python ##

**1 - Setting up**

Create a virtual environment
```
...\> py -m venv project-name
```
Activate the environment
```
...\> project-name\Scripts\activate.bat
```
Version info 
> python: 3.8.4.final.0  
> pip: 21.3.1  
 
<!-- Install django
```
py -m pip install Django
``` -->

**2 - Install package** `pip install <package>`
> **Django==4.0.1**  
> **djangorestframework==3.13.1**  
> **gunicorn==20.1.0**  
> asgiref==3.4.1  
> backports.zoneinfo==0.2.1  
> dj-database-url==0.5.0  
> dj-static==0.0.6   
> django-heroku==0.3.1  
> django-toolbelt==0.0.1   
> psycopg2==2.9.3  
> pytz==2021.3  
> sqlparse==0.4.2  
> static3==0.7.0  
> tzdata==2021.5  
> whitenoise==5.3.0  

or in [./requirements.txt](./requirements.txt)

**3 - Deploy**
Create requirements.txt
```
pip freeze > requirements.txt
```
Create app
```
heroku create <app-name>
```
Add heroku remote
```
heroku git:remote -a <app-name>
```
Push app
```
git push heroku master
```

**4 - Some config if app not run**
- heroku config:set DISABLE_COLLECTSTATIC=1 // Not sure if this was necessary eventually as I guess problem with collect static was due to no module found error.

<!--
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
-->