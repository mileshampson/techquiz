import pymongo
import os

def __getDbConnection():
    global __connection
    if __connection is None:
        __connection = pymongo.Connection()
    return __connection['techquiz']


# internals

__connection = None


    