import os 

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = '12345'
    QUOTE_URL = "http://quotes.stormconsultancy.co.uk/random.json"

    EMAIL = "tomwere9@gmail.com"
    PASSWORD = "tom97?"
  
class TestConfig(Config):
    pass


class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    MAIL_USE_SSL = True
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True 
    MAIL_USERNAME = "tomwere9@gmail.com"
    MAIL_PASSWORD ="svsss"

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    

class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mark:Wildwave123@localhost/blog'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}