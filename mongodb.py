from pymongo import MongoClient

connection = MongoClient()
db = connection["the-zoo"]
