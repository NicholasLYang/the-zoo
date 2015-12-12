from pymongo import MongoClient


connection = MongoClient()
db = connection["the-zoo"]
users = db['users']
posts = db['posts']
'''
<----------------- USER ----------------->
'''
# Everything should be escaped/hashed by now
def addUser(firstName, lastName, uname, pword, email):
    # Searches for user in database. If there's no user by that username, then it'll be added
    result = findUserbyUsername(uname)
    if result == 2:
        userId = getNextRowId("users") + 1
        db.users.insert(
        {"first name": firstName,
        "last name": lastName,
        "username": uname,
        "password": pword,
        "email":email,
        "user id": userId})
    else:
        return "Sorry, username is taken"

def findUserbyUsername(uname):
    result = db.users.find_one({"username": uname})
    if (result == None):
        return 2
    return result

def findUserbyName(firstName, lastName):
    result = db.users.find_one({"first name": firstName, "last name": lastName})
    return result

# 0 is good, 1 is wrong password, 2 is user does not exist
def authenticate(uname, pword):
    user = findUser(uname)
    if user == 2:
        return 2
    if (user['password'] == pword):
        return 0
    else:
        return 1

def removeUsername(uname):
    db.users.remove(
        {"username" : uname})
def removeUserId(userId):
    db.users.remove(
        {"user id": userId})
    
'''
<----------------- POSTS ----------------->
'''
# commentIds is a list of comment ids 
def addPost(authorId, title, text):
    commentIds = []
    postId = getNextRowId("posts") + 1
    db.posts.insert(
        {"post id": postId,
        "author id": authorId,
        "title":title,
        "text":text,
        "comment ids":commentIds})

# Returns a cursor with posts that have a certain title. 
def findPostsbyTitle(title):
    results = db.posts.find(
        {"title":title})
    return result


# Finds a post by its post id
def findPostbyPostId(postId):
    result = db.posts.find_one(
        {"post id":postId})
    return result
# Returns the cursor to the posts written by an id
def findUserIdsPosts(id):
    result = db.posts.find(
    {"authorId":id})
    return result

# Returns the cursor to the posts written by a username
def findUsernamesPosts(username):
    result = db.posts.find(
        {"author username": username})
    return result
'''
<----------------- COMMENTS ----------------->
'''
def addComment (postId, authorId, text):
    commentId = getNextRowId("comments") + 1
    db.comments.insert(
        {"comment id":commentId,
        "author id": authorId,
        "text":text,
        "postId": postId})
    

def findUsernamesComments(username):
    result = db.comments.find(
        {"author username": username})
    
def findIdsComments(authorId):
    result = db.comments.find(
        {"author id": authorId})

'''
<----------------- MISC ----------------->
'''

# Totally didn't steal this from the Storybored softdev project
def getNextRowId(collection):
    cursor = db[collection].find().sort([('rowid', -1)]).limit(1)
    try:
        rid = cursor[0]['rowid']
    except (IndexError, KeyError):
        rid = 0
    return rid

'''
<----------------- COMMUNITY ----------------->
'''
def addCommunity(commName, lastName, userList, accessCode):
    # Searches for user in database. If there's no user by that username, then it'll be added
    result = findCommunitybyName(commName)
    if result == 2:
        commId = getNextRowId("communities") + 1
        db.users.insert(
        {"community name": commName,
        "community id":  commId,
        "user list": userList,
        "access code": accessCode})
    else:
        return "Sorry, community exists"

def addUserToCommunity(community_ID, userID):
	userList = db['communities'].find(
		{"community id": community_ID})[0]['user list']
	userList.add(userID)
	db['communities'].update({"community id": community_ID}, 
							{"user list": userList})

def findCommunitybyName(commName):
    result = db.communities.find_one({"community name": commName})
    if (result == None):
        return 2
    return result


def removeCommunity(commID):
    db.communities.remove(
        {"community id": commID})