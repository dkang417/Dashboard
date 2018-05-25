from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt 
from .models import *

# Create your views here.

def index(request):
	#protects our url from people not logged in
	# if request.session.get('id') != None:
	# 	return redirect('/dashboard')

	return render(request,'dashboard/index.html')

def process(request):
	return render(request,'dashboard/register.html')

def register(request):
    User.objects.validate(request)
    return redirect("/dashboard")


def login(request):
	if request.method == "POST":

		email = request.POST['email']
		password = request.POST['password']
		user = User.objects.filter(email=email)
		#check to see if there is a matching user
		if len(user) > 0: 
			#we have a user so check password
			checkpassword = bcrypt.checkpw(password.encode(), user[0].password.encode())
			if checkpassword:
				request.session['id'] = user[0].id 
				return redirect('/dashboard')
		
			
			#user does not exist
		messages.error(request,'incorrect user/password combination')
		return redirect('/')
	else: 
		return render(request,'dashboard/login.html')

def logout(request):
	request.session.clear()
	return redirect('/')

def dashboard(request):
	if request.session.get('id') == None:
		return redirect('/')
	user = User.objects.get(id=request.session['id'])

	context = {
		'user':user
	}
	return render(request, 'dashboard/dashboard.html', context)

