import datetime
import distdata.connection
    
def writeMessage(messageText):
    messagesCollection = __getMessagesCollection()
    entry = messagesCollection.find_one(messageText)
    if entry is None:
        entry = {"_id": messageText,
                 "message": messageText,
                 "count": 0 }
    entry["count"]+=1
    entry["date"] = datetime.datetime.utcnow()
    messagesCollection.save(entry)
    
def get_messages():
    messagesCollection = __getMessagesCollection()
    return messagesCollection.find().sort("date")

# internals

def __getMessagesCollection():
    return distdata.connection.__getDbConnection().messages

if __name__ == '__main__':
    for entry in get_messages():
        print entry