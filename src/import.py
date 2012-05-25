import sys, os
import distdata.questions

def _getBasePath():
    encoding = sys.getfilesystemencoding()
    (head, tail) = os.path.split(os.path.dirname(unicode(__file__, encoding)))
    # (head, tail) = os.path.split(head)
    return head


if __name__ == '__main__':
    filename = _getBasePath()+"/questions.json"
    host = 'prodbox'
    print "importing techquiz.questions from "+filename+" to mongodb on "+host
    distdata.questions.importQuestions(host, filename)
    print "done"