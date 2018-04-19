
class Config(object):
	DEBUG = False
	TESTING = False
	MYSQL_DATABASE_USER = ""
	MYSQL_DATABASE_PASSWORD = ""

class ProductionConfig(Config):
	MYSQL_DB = 'chickadees'

class DevelopmentConfig(Config):
	DEBUG = True
	MYSQL_DB = 'chickadeesTesting'

class TestingConfig(Config):
	TESTING = True
	WTF_CSRF_ENABLED = False
	DEBUG = False
	MYSQL_DB = 'chickadeesTesting'

config = {
	'development': DevelopmentConfig,
	'production': ProductionConfig,
	'testing': TestingConfig
}
