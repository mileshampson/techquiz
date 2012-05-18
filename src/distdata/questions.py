import distdata.connection

#
# terminology derived from http://en.wikipedia.org/wiki/Multiple_choice
#
# question._id             <- unique id, int, start from 1, sequential
# question.stem            <- beginning part of the item that presents the item as a problem to be solved, can be an incomplete statement
# question.key             <- correct answer
# question.distractors[]   <- incorrect options

def getQuestion(qid=0):
    if qid == 0:
        return __getQuestionsCollection().find_one()
    else:
        return __getQuestionsCollection().find_one({"_id":qid})

def addNewQuestion(stem, key, distractors):
    bson = __encodeQuestion(distdata.connection.counterIncAndGet("questions"), stem, key, distractors)
    __getQuestionsCollection().save(bson)

def updateQuestion(qid, stem, key, distractors):
    bson = __encodeQuestion(qid, stem, key, distractors)
    __getQuestionsCollection().save(bson)
    
def deleteQuestion(qid):
    __getQuestionsCollection().remove({"_id":qid})
    
def __getQuestionsCollection():
    return distdata.connection.getTechquizDb().questions 

def __encodeQuestion(qid, stem, key, distractors):
    bson = {
            "_id": qid,
            "stem": stem,
            "key": key, 
            "distractors":distractors,
                }
    return bson

if __name__ == '__main__':
    q = getQuestion(qid='2')
    print q
    print q["stem"]
    print q["key"]
    print q["distractors"][0]
    print q["distractors"][1]
    print q["distractors"][2]
    
            