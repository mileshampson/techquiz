import pymongo
import os

def getTechquizDb():
    global __connection
    if __connection is None:
        __connection = pymongo.Connection()
    return __connection['techquiz']

def counterIncAndGet(name):
    ret = getTechquizDb().counters.find_and_modify(query={"_id":name},update={"$inc" : {"next":1}}, upsert=True, new=True )
    return ret["next"]


# internals

__connection = None

if __name__ == '__main__':
    print counterIncAndGet("test1")
    print counterIncAndGet("test1")
    print counterIncAndGet("test1")
    