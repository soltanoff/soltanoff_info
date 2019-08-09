# Simple Blog & File server

This server consist of the personal blog and the file storage for some needs.

For the article content editor used CKEditor.

Create django\_srv\local\_settings.py with following content:
```python
# from .settings import INSTALLED_APPS, MIDDLEWARE
# Uncomment first line for development server

SECRET_KEY = 'Your secret key'

DEBUG = True  # False if your want to use fastpost in production

ALLOWED_HOSTS = []  # for development
ALLOWED_HOSTS = ['*']  # for docker-compose
ALLOWED_HOSTS = ["your-production-domain"]  # for production

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pyftp_db',
        'USER': 'dbuser',
        'PASSWORD': 'dbpassword',
        'HOST': 'mysql',  # Or an IP Address that your DB is hosted on
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8',
            'use_unicode': True,
        },
    }
}

# if you want to use debug_toolbar (dev server only)
INSTALLED_APPS.append('debug_toolbar')
MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')

```

Fill your database and run Django development server:
```
$ pip3 install -r requirements.txt
$ python3 manage.py migrate
$ python3 manage.py collectstatic
```

To run with a docker compose:
```
docker-compose up
```
