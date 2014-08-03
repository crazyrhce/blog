from django.http import HttpResponse
import datetime
import sys
import os
from django.template import Template,Context
from django.shortcuts import render_to_response,redirect

def home(request):
	return HttpResponse("Hello Domob")
'''
def test(request,w):
	#return HttpResponse("Hello test %s" % w)
	t = Template('My name is {{name}}.')
	c = Context({'name':w})
	print c
	return HttpResponse(t.render(c))
'''
def test(request,w):
	#return render_to_response("test.html",{'name':w})
	a = 5
	b = [1,2,3,4,5]
	return render_to_response("test.html",{'name':w,'a':a,'b':b})

def test1(request):
	#return HttpResponse("Hello test1 %s" % datetime.datetime.now())
	#return HttpResponse("Hello test1 %s" % os.listdir("./jeapblog"))
	return HttpResponse(os.uname())

from .models import Blog
from django.template import RequestContext
def blog_create_form(request):
	return render_to_response("create.html",context_instance=RequestContext(request))

def blog_create(request):
	b = Blog()
	#b.title = "new blog"
	b.title = request.POST['title']
	b.content = request.POST['content']
	b.save()
	return redirect("/list")

def blog_list(request):
	blogs = Blog.objects.filter().order_by('-id')
	return render_to_response("list1.html",{'blogs':blogs})

def blog_update(request,id):
	b = Blog.objects.get(id=int(id))
	return render_to_response("update.html",{'b':b },context_instance=RequestContext(request))
	#b.title = "update blog"
	#b.save()
	#return redirect("/list")

def blog_update_save(request,id):
	b = Blog.objects.get(id=int(id))
	b.title = request.POST['title']
	b.content = request.POST['content']
	b.save()
	return redirect("/list")

def blog_delete(request,id):
	Blog.objects.get(id=int(id)).delete()
	return redirect("/list")

