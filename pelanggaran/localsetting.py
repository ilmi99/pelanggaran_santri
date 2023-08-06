import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DATABASE = {
    'default' : {
            'ENGINE' : 'django.db.backend.sqlite3',
            'NAME' : os.path.join(BASE_DIR, 'db.sqlite'),    
}
}