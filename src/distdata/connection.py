import pymongo
import os

def getConnection(host='localhost'):
    global __connection
    if __connection is None:
        __connection = pymongo.Connection(host)
    return __connection
    
def getTechquizDb(host='localhost'):
    return getConnection(host)['techquiz']

def counterIncAndGet(name, host='localhost'):
    ret = getTechquizDb(host).counters.find_and_modify(query={"_id":name},update={"$inc" : {"next":1}}, upsert=True, new=True )
    return ret["next"]


# internals

__connection = None

if __name__ == '__main__':
    print counterIncAndGet("test1")
    print counterIncAndGet("test1")
    print counterIncAndGet("test1")
    