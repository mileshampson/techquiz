import pymongo
import os

def getConnection():
    global __connection
    if __connection is None:
        __connection = pymongo.Connection()
    return __connection
    
def getTechquizDb():
    return getConnection()['techquiz']

def counterIncAndGet(name):
    ret = getTechquizDb().counters.find_and_modify(query={"_id":name},update={"$inc" : {"next":1}}, upsert=True, new=True )
    return ret["next"]


# internals

__connection = None

if __name__ == '__main__':
    print counterIncAndGet("test1")
    print counterIncAndGet("test1")
    print counterIncAndGet("test1")
    