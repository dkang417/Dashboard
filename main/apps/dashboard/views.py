from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt 
from .models import *

# Create your views here.

def index(request):

	return render(request,'dashboard/index.html')

def process(request):
	return render(request,'dashboard/register.html')

def register(request):
    User.objects.validate(request)
    return redirect("/")


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
		return redirect('/login')
	else: 
		return render(request,'dashboard/login.html')

def logout(request):
	request.session.clear()
	return redirect('/')

def dashboard(request):
	if request.session.get('id') == None:
		return redirect('/')

	user = User.objects.get(id=request.session['id'])
	users = User.objects.all()
	context = {
		'user':user,
		'users':users
	}

	return render(request, 'dashboard/dashboard.html', context)

def adduser(request):
	return render(request, 'dashboard/adduser.html')

def createuser(request):
	User.objects.validate(request)
	return redirect('/dashboard')

def editid(request,id):
	user = User.objects.get(id=id)
	context = {
		'user' : user
	}
	return render(request, 'dashboard/edituser.html', context)

def updateid(request,id):
	user = User.objects.get(id=id)
	first_name = request.POST["first_name"]
	last_name = request.POST["last_name"]
	email = request.POST["email"]
	user_level = request.POST["user_level"]

	user.first_name = first_name
	user.last_name = last_name
	user.email = email 
	user.user_level = user_level
	user.save()
	messages.success(request,"user successfully updated")
	
	return redirect('/dashboard')

def updatepassword(request,id):
	user = User.objects.get(id=id)
	password = request.POST["password"]
	confirm = request.POST["confirm_password"]
	hashed_pw = bcrypt.hashpw(password.encode(),bcrypt.gensalt())
	if request.POST["password"] != request.POST["confirm_password"]:
		messages.error(request,"passwords do not match")

	user.password = hashed_pw
	user.save()
	messages.success(request,"password successfully updated")
	return redirect('/dashboard')

def deleteuser(request,id):
	user = User.objects.get(id=id)
	context = {
		'user' : user
	}
	return render(request,'dashboard/deleteuser.html', context)

def removeuser(request, id):
	user = User.objects.get(id=id)
	user.delete()
	return redirect('/dashboard')

def userinfo(request, id): 
	user = User.objects.get(id=id)
	context = {
		'user': user
	}
	return render(request, 'dashboard/userinfo.html', context)