import sys, os
import distdata.questions

def _getBasePath():
    encoding = sys.getfilesystemencoding()
    (head, tail) = os.path.split(os.path.dirname(unicode(__file__, encoding)))
    # (head, tail) = os.path.split(head)
    return head


if __name__ == '__main__':
    # copy prod database to dev database
    print "copying techquiz database"
    result = distdata.connection.getConnection().copy_database('techquiz', 'techquiz', from_host='prodbox')
    print result
    filename = _getBasePath()+"/questions.json"
    print "exporting techquiz.questions to "+filename
    distdata.questions.export(filename)
    print "done"