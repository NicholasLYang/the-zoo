from pymongo import MongoClient

connection = MongoClient()
db = connection["the-zoo"]
users = db['users']

# Everything should be escaped/hashed by now
def addUser(uname, pword):
    db.users.insert(
        {
        "username": uname,
        "password": pword
        })
    

def findUser(uname):
    result = db.users.find_one({"username": uname})
    return result['username']

# 0 is good, 1 is wrong password, 2 is user does not exist
def authenticate(uname, pword):
    user = findUser(uname)
    if (user['password'] == pword):
        return 0
