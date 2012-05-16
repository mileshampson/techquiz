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

def index(request):
    t = loader.get_template('index.html')
    c = Context({"question":distdata.questions.getQuestion()})
    return HttpResponse(t.render(c))

def new(request):
    if request.method == 'GET':
        t = loader.get_template('new.html')
        c = RequestContext(request, {})
        return HttpResponse(t.render(c))
    else:
        stem = request.REQUEST["stem"]
        key = request.REQUEST["key"]
        distractors = []
        distractors.append(request.REQUEST["distractor1"])
        distractors.append(request.REQUEST["distractor2"])
        distractors.append(request.REQUEST["distractor3"])
        distdata.questions.addNewQuestion(stem, key, distractors)
        return redirect("/")
    
def statistics(request):
    t = loader.get_template('statistics.html')
    c = Context({ "messages":distdata.messages.get_messages() })
    return HttpResponse(t.render(c))

    