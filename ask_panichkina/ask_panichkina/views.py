# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import hashlib
import os
import json
import datetime
from ask_panichkina.models import Question, Tag, Answer, Profile, Rate_answer, Rate_profile, Rate_question
#@csrf_exempt
#def helloworld(request):
#	output = '<b>Hello World!Broooo</b><br />'
#	if request.method == 'GET':
#		output += 'Get query: '
#		for x in request.GET:
#			output+= '<br/>'
#			params = request.GET.getlist(x)
#			output += '<b>' + x + '</b>' + ':'
#			for param in params:
#				output += '<br/>' + param
#	else:
#		output += 'Post query: '
#		for x in request.POST:
#			output+= '<br/>'
#			params = request.POST.getlist(x)
#			output += '<b>' + x + '</b>' + ':'
#			for param in params:
#				output += '<br/>' + param
#	html = "<html><body>%s</body></html>" % output
#	return HttpResponse(html)


# def questions(request):

#   return render(request, 'index.html',())

questions = Question.objects.all()

def question(request, id):
    data = {
        'id' : int(id),
    }
    return HttpResponse(json.dumps(data), content_type = 'application/json')

def home(request):
    context = {
        'questions':Question.objects.all()[:10]
    }
    return render(request,'index.html',context)




def index (request):
    return render(request, 'index.html', ())

def signup(request):
    return render(request, 'signup.html',())

def login(request):
    return render(request, 'login.html', ())

def ask_question(request):
    return render(request, 'ask_question.html', ())





