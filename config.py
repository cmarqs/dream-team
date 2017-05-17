"""
Conteins the application configurations.

It is good practice to specify configurations for different environments. In the
file above, we have specifed configurations for development, which we will use 
while building the app and running it locally, as well as production, which 
we will use when the app is deployed.
"""


class Config(object):
    """
    Common configuration
    """
    pass


class DevelopmentConfig(Config):
    """
    Development configuration
    """
    DEBUG = True
    SQLALCHEMY_ECHO = True  # Allow SQLAlchemy to log errors, helping the debug.


class ProductionConfig(Config):
    """
    Production enviroment configurations
    """
    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
