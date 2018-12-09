import os

class Config:
    SECRET_KEY = '6492e3bac392361bd157f4cdf0feb4b6'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'

    DB_USERNAME = 'sa'
    DB_PASSWORD = 'password'
    DB_NAME = 'blogdb'

    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@localhost:3306/{DB_NAME}'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://sa:password@localhost:3306/blogdb'

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')