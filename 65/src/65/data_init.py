import pymongo
import datetime


def data_init():
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client.database65
    db.order.delete_many({})
    return db


db = data_init()
