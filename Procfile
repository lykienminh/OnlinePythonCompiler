release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input
release: gunicorn pythoncompiler9.py:application 

web: gunicorn pythoncompiler9.py