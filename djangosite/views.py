from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache
import os, simplejson
from django.core.mail import send_mail
import distdata.messages

def admin(request):
    t = loader.get_template('admin.html')
    ctxdata = {}
    c = Context(ctxdata)
    return HttpResponse(t.render(c))
    
def index(request):
    t = loader.get_template('index.html')
    ctxdata = {}
    c = Context(ctxdata)
    return HttpResponse(t.render(c))

def statistics(request):
    t = loader.get_template('statistics.html')
    c = Context({ "messages":distdata.messages.get_messages() })
    return HttpResponse(t.render(c))

    