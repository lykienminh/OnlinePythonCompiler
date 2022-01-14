# OnlinePythonCompiler
Online Python Compiler 

Python Compiler API /python

heroku git:remote -a pythoncompiler9

git remote show heroku

..\Scripts\activate

1 - heroku config:set DISABLE_COLLECTSTATIC=1 // Not sure if this was necessary eventually as I guess problem with collect static was due to no module found error.

2 - pip freeze > requirements.txt // to make sure rest_framework is included in the file.

3 - then proceeding with the git push.

4 - heroku config:set DISABLE_COLLECTSTATIC

5 - heroku run python manage.py collectstatic