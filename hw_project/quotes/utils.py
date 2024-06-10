from pymongo import MongoClient


def get_mongodb():
    client = MongoClient("mongodb+srv://user1:567234@tetianakobzar.2kizr3f.mongodb.net/?retryWrites=true&w=majority&appName=TetianaKobzar")
    db = client.TetianaKobzar
    return db