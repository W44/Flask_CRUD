class Config:
    """
    Configs which will be common in all environments.
    """
    SQLALCHEMY_DATABASE_URI = "sqlite:///f1.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 't1NP63m4wnBg6nyHYKfmc2TpCOGI4nss'


class DevConfig(Config):
    """
    Dev specific Configs.
    """
    pass


class ProdConfig(Config):
    """
    Production specific Configs.
    """
    pass
