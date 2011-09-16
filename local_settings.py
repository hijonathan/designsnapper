DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',    # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'chief_db',                      # Or path to database file if using sqlite3.
        'USER': 'chief',                         # Not used with sqlite3.
        'PASSWORD': 'chief',                     # Not used with sqlite3.
        'HOST': '127.0.0.1',                              # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                              # Set to empty string for default. Not used with sqlite3.
    }
}
