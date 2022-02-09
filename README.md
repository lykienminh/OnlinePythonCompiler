# OnlinePythonCompiler

## Python Compiler API /python

1.Setting up a virtual environment 

Create a virtual environment
```
...\> py -m venv project-name
```
Activate the environment
```
...\> project-name\Scripts\activate.bat
```



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