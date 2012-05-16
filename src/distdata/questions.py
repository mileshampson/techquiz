import distdata.connection

#
# terminology derived from http://en.wikipedia.org/wiki/Multiple_choice
#
# question._id             <- unique id, int, start from 1, sequential
# question.stem            <- beginning part of the item that presents the item as a problem to be solved, can be an incomplete statement
# question.key             <- correct answer
# question.distractors[]   <- incorrect options

def getQuestion():
    return __getQuestionsCollection().find_one()

def addNewQuestion(stem, key, distractors):
    bson = __encodeQuestion(distdata.connection.counterIncAndGet("questions"), stem, key, distractors)
    __getQuestionsCollection().save(bson)
    
def __getQuestionsCollection():
    return distdata.connection.getTechquizDb().questions 

def __encodeQuestion(qid, stem, key, distractors):
    bson = {
            "_id": qid,
            "id": qid,
            "stem": stem,
            "key": key, 
            "distractors":distractors,
                }
    return bson

if __name__ == '__main__':
    addNewQuestion("Who is Doug Lea?", "Author of JSR166, Introduced concurrency utilities to JDK",["Invented Java in 1994","Author of The Java Handbook","Author of Effective Java"])
    addNewQuestion("This is mostly happens in time sharing systems in which the process which requires a resource is waiting for another process to finish and to release the resources, but the other process holding the resources for long time (almost for forever) and the process that requires small time slot goes on waiting. Such situation is called?","starvation",["deadlock","Excessive context switching","Race condition"]) 
    for question in __getQuestionsCollection().find():
        print question
        
            