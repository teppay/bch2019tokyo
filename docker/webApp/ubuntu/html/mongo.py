#usr/bin/env python

from pymongo import MongoClient

def get_stab():
    username   = "master"
    password   = "master"
    client     = MongoClient("mongodb://master:master@40.114.77.68:27032/")
    database   = client["nem_suspicious_txs"]
    collection = database["c20181231"]
    document   = collection.find_one()

    print(document)
    return document

if __name__ == '__main__':
    get_stab()
