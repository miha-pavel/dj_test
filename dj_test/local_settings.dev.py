DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dj_test',
        'USER': 'postgres',
        # 'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
