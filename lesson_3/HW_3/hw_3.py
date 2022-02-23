from pymongo import MongoClient
from pprint import pprint
from pymongo.errors import DuplicateKeyError as dke

client = MongoClient('localhost', 27017)

db = client['users1502']    # database
persons = db.persons        # collection
