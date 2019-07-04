
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfiguration:

    DEBUG = True
    TESTING = False
    EXPLAIN_TEMPLATE_LOADING = False

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'details.db')   
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY =  "SuperSecretKey"





        
