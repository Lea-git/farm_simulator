from pymongo import MongoClient
from db import MONGO_CONFIG

def get_client():
    return MongoClient(MONGO_CONFIG['host'], MONGO_CONFIG['port'])

def get_database():
    client = get_client()
    return client[MONGO_CONFIG['database']]

def get_collection(name):
    db = get_database()
    return db[name]

# Exemple : récupérer les machines
def get_all_machines():
    collection = get_collection('machines')
    return list(collection.find())