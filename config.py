import os

class Config:

    
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:malcomiz0582@localhost/sql'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
#  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgres://draofkltplxorw:da3194c3eca4ba97b045cfaf76204a213ea48089ad5a40c0e763162cd0c58b2f@ec2-107-20-127-127.compute-1.amazonaws.com:5432/d4tf780cr625od"
    


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:malcomiz0582@localhost/sql'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}