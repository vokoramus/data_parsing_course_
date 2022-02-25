from pymongo import MongoClient
from pprint import pprint
from pymongo.errors import DuplicateKeyError as dke

client = MongoClient('localhost', 27017)

db = client['users1502']    # database
persons = db.persons        # collection
books = db.books            # collection

# =================  insert_one  =================
try:
    persons.insert_one({"_id": 100,
                        "author": "Peter2",
                        "age": 38,
                        "text": "is cool! Wildberry",
                        "tags": ['cool', 'hot', 'ice'],
                        "date": '14.06.1983'})
except dke:
    print('Duplicate key error collection')

# =================  insert_many  =================
# persons.insert_many([{"author": "John",                               # Добавляем несколько документов в базу
#                "age" : 29,
#                "text": "Too bad! Strawberry",
#                "tags": 'ice',
#                "date": '04.08.1971'},
#
#                     {"_id": 123,
#                         "author": "Anna",
#                "age" : 36,
#                "title": "Hot Cool!!!",
#                "text": "easy too!",
#                "date": '26.01.1995'},
#
#                    {"author": "Jane",
#                "age" : 43,
#                "title": "Nice book",
#                "text": "Pretty text not long",
#                "date": '08.08.1975',
#                "tags":['fantastic', 'criminal']}])

# =================  find  =================
# for doc in persons.find({'author': 'Peter2'}):
#     pprint(doc)

# for doc in persons.find({'author': 'Peter2', '_id': 564843135186}):
#     pprint(doc)

# for doc in persons.find({'$or': [{'author': 'Peter2'}, {'age': 43}]}):
#     pprint(doc)

# for doc in persons.find({'age': {'$lte': 35}}):
#      pprint(doc)

# for doc in persons.find({'$or': [{'author': 'Peter2'}, {'age': {'$lte': 35}}]}):
#     pprint(doc)

# for doc in persons.find({'author': {'$regex': 'J'}}):
#     pprint(doc)

# =================  find_one  =================
# result = persons.find_one({'author': 'Peter2'})
# if result:
#     print('Found')
#     print(result)
# else:
#     print('Not Found')

##new_data = {
##    "author": "Andrey",
##               "age" : 28,
##               "text": "is hot!",
##               "date": '11.09.1991'}

# =================  update_one  =================
# persons.update_one({'author': 'Peter2'}, {'$set': new_data})

# =================  replace_one  =================
# persons.replace_one({'author': 'Andrey'}, new_data)

# =================  delete_one  =================
# persons.delete_one({'author': 'Peter2'})

# result = persons.delete_one({})

# =================  delete_many  =================
# result = persons.delete_many({})


# result = list(persons.find({'author': 'Peter2'}))
# pprint(result)

for doc in persons.find({}):
    pprint(doc)

print(len(list(persons.find({}))))