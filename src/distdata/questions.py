import distdata.connection
import simplejson
#
# terminology derived from http://en.wikipedia.org/wiki/Multiple_choice
#
# question._id             <- unique id, int, start from 1, sequential
# question.stem            <- beginning part of the item that presents the item as a problem to be solved, can be an incomplete statement
# question.key             <- correct answer
# question.distractors[]   <- incorrect options

def getQuestionGivenTag(tag):
    return __getQuestionsCollection().find_one({"tags":tag})

def getQuestion(qid=0):
    if qid == 0:
        return __getQuestionsCollection().find_one()
    else:
        return __getQuestionsCollection().find_one({"_id":qid})

def addNewQuestion(stem, key, distractors, explanation, tags):
    bson = __encodeQuestion(distdata.connection.counterIncAndGet("questions"), stem, key, distractors, explanation, tags)
    __getQuestionsCollection().save(bson)

def updateQuestion(qid, stem, key, distractors, explanation, tags):
    bson = __encodeQuestion(qid, stem, key, distractors, explanation, tags)
    __getQuestionsCollection().save(bson)
    
def deleteQuestion(qid):
    __getQuestionsCollection().remove({"_id":qid})

# this may be done using mongodump and bsondump, but bsondump is not available in my mongodb version
def export(filename):
    questionList = []
    for question in __getQuestionsCollection().find():
        questionList.append(question)
    fd = open(filename, 'w')
    simplejson.dump(questionList, fd, indent=True)
    fd.close()

def importQuestions(host, filename):
    fd = open(filename, 'r')
    questionList = simplejson.load(fd)
    fd.close()
    for question in questionList:
        # mandatory fields
        stem = question["stem"]
        key = question["key"]
        distractors = question["distractors"]
        # recently introduced or optional fields
        if "explanation" in question:
            explanation =  question["explanation"]
        else:
            explanation = ""
        if "tags" in question:
            tags =  question["tags"]
        else:
            tags = []
        bson = __encodeQuestion(distdata.connection.counterIncAndGet("questions", host), stem, key, 
                            distractors, explanation, tags)
        __getQuestionsCollection(host).save(bson)   
    
def __getQuestionsCollection(host='localhost'):
    return distdata.connection.getTechquizDb(host).questions 

def __encodeQuestion(qid, stem, key, distractors, explanation, tags):
    # convert tags to lower case
    tags = [x.lower() for x in tags]
    bson = {
            "_id": qid,
            "stem": stem,
            "key": key, 
            "distractors":distractors,
            "explanation":explanation,
            "tags":tags,
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
    
            