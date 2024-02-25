import pymongo


SECRET_KEY = b'\x1e\xc6\x0f\x94_\xbe\x0c\x1f\x05*\xeeaS\xd9"\xa0'

TEMPLATE_FOLDER = '../templates'

client = pymongo.MongoClient('localhost', 27017, username='admin', password='admin')
db = client.user_login_system
