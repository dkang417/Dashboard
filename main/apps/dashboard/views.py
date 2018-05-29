from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt 
from .models import *


def index(request):
	return render(request,'dashboard/index.html')

def process(request):
	return render(request,'dashboard/register.html')

def register(request):
    User.objects.validate(request)
    return redirect("/process")

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
	User.objects.validateUserInfo(request,id)
	return redirect('/users/edit/{}'.format(id))

def updatepassword(request,id):
	User.objects.validatePassword(request,id)
	return redirect('/users/edit/{}'.format(id))

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
	messages= Message.objects.filter(message_for=id)
	comments = Comment.objects.all()
	context = {
		'user': user,
		'message': messages,
		'comments' : comments
	}
	return render(request, 'dashboard/userinfo.html', context)

def makemessage(request, id):
	Message.objects.validateMessage(request,id)
	return redirect('/users/show/{}'.format(id))

def makecomment(request,user_id,message_id):
	Comment.objects.validateComment(request,user_id,message_id) 
	return redirect('/users/show/{}'.format(user_id))

def editprofile(request):
	user = User.objects.get(id=request.session['id'])
	context = {
		'user':user
	}
	return render(request, 'dashboard/editmyprofile.html', context)
def updatemyprofile(request):
	User.objects.validateMyinfo(request)
	return redirect('/users/edit')

def updatemypassword(request):
	User.objects.validateMypassword(request)
	return redirect('/users/edit')

def editdescription(request):
	User.objects.validateDescription(request)
	return redirect('/users/edit')