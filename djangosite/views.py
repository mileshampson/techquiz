from django.template import RequestContext, loader, Context
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache
import os, simplejson
from django.core.mail import send_mail
import distdata.questions
import distdata.messages

def admin(request):
    t = loader.get_template('admin.html')
    ctxdata = {}
    c = Context(ctxdata)
    return HttpResponse(t.render(c))

def category_select(request):
    t = loader.get_template('category_select.html')
    ctxdata = {}
    c = Context(ctxdata)
    return HttpResponse(t.render(c))

def about(request):
    t = loader.get_template('about.html')
    ctxdata = {}
    c = Context(ctxdata)
    return HttpResponse(t.render(c))

@never_cache
def index(request, qid=0):
    t = loader.get_template('index.html')
    ctxdata = {}
    qid = int(qid)
    question = distdata.questions.getQuestion(qid)
    ctxdata["question"] = question
    ctxdata["question_json"] = simplejson.dumps(question)
    if question:
        qid = question["_id"]
    ctxdata["qid"] = qid
    ctxdata["prevqid"] = qid - 1
    ctxdata["nextqid"] = qid + 1
    return HttpResponse(t.render(Context(ctxdata)))

def __getPromRequest(request):
    stem = request.REQUEST["stem"]
    key = request.REQUEST["key"]
    distractors = []
    distractors.append(request.REQUEST["distractor1"])
    distractors.append(request.REQUEST["distractor2"])
    distractors.append(request.REQUEST["distractor3"])
    explanation = request.REQUEST["explanation"]
    tags = request.REQUEST["tags"].split(None, 5)
    return (stem, key, distractors, explanation, tags)

@never_cache
def new(request):
    if request.method == 'GET':
        t = loader.get_template('new.html')
        c = RequestContext(request, {})
        return HttpResponse(t.render(c))
    else:
        (stem, key, distractors, explanation, tags) = __getPromRequest(request)
        distdata.questions.addNewQuestion(stem, key, distractors, explanation, tags)
        return redirect("/questions")

@never_cache
def edit(request):
    if request.method == 'GET':
        t = loader.get_template('edit.html')
        qid = int(request.REQUEST["qid"])
        ctxdata = {}
        ctxdata["question"] = distdata.questions.getQuestion(qid)
        ctxdata["qid"] = qid
        c = RequestContext(request, ctxdata)
        return HttpResponse(t.render(c))
    else:
        qid = int(request.REQUEST["qid"])
        (stem, key, distractors, explanation, tags) = __getPromRequest(request)
        distdata.questions.updateQuestion(qid, stem, key, distractors, explanation, tags)
        return redirect("/questions/"+str(qid))

@never_cache
def delete(request):
#    if request.method == 'GET':
#        qid = int(request.REQUEST["qid"])
#        distdata.questions.deleteQuestion(qid)
#        return redirect("/questions/"+str(qid))
    t = loader.get_template('delete.html')
    return HttpResponse(t.render(Context({})))

def statistics(request):
    t = loader.get_template('statistics.html')
    c = Context({ "messages":distdata.messages.get_messages() })
    return HttpResponse(t.render(c))

    