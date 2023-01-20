class Config:
    DEBUG = True
    SECRET = 'test'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./../data/movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # JSON_AS_ASCII = False
    RESTX_JSON = {'ensure_ascii': False}
    # RESTFUL_JSON = {'ensure_ascii': False}
