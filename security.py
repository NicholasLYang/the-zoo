import hashlib

m = hashlib.sha256()

def hash(input):
    m.update(input)
    return m.digest()

# Tests whether an unhashed username corresponds to a hash
def testUsername(username, hash):
    m.digest()
    hashUsername = m.update(username)
    return hashUsername == hash
    
