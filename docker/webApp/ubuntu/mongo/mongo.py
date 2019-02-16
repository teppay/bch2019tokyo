#usr/bin/env python

from pymongo import MongoClient
username   = "master"
password   = "master"
#client     = MongoClient("mongodb://%s:%s@40.114.77.68:27032/".format(username,password))
client     = MongoClient("mongodb://master:master@40.114.77.68:27032/")
database   = client["nem_suspicious_txs"]
collection = database["c20181231"]
document   = collection.find_one()

print(document)

#print(type(client))
#print(client)
#print("")
#print(type(database))
#print(database)
#print("")
#print(type(collection))
#print("")
#print(type(collection.find_one()))
#print(collection.find_one())
