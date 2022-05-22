import os 

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = '12345'
    QUOTE_URL = "http://quotes.stormconsultancy.co.uk/random.json"

    EMAIL = "tomwere9@gmail.com"
    PASSWORD = "tom97"
    MAIL_USE_SSL = True
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True 
    MAIL_USERNAME = "tomwere9@gmail.com"
    MAIL_PASSWORD ="svsss"
  
class TestConfig(Config):
    pass


class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    

    SQLALCHEMY_DATABASE_URI = 'postgresql://pguwimdgtaimag:cd6c3a9e84fad2cb2cf2b19678d08d290ccacedd2001eba637a75ef2ae2786da@ec2-34-231-177-125.compute-1.amazonaws.com:5432/d8jt5mpu635vfd'
    

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