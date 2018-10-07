import os

class Config:
    BASE_URL_SOURCES = "https://newsapi.org/v2/sources?apiKey={}"
    BASE_URL_ARTICLES = "https://newsapi.org/v2/top-headlines?sources={}&apiKey={}"
    SECRET_KEY = os.environ.get('SECRET_KEY')
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}

