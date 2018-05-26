from __future__ import unicode_literals

from django.db import models
from django.contrib import messages
import bcrypt



class Description(models.Model):
    description = models.TextField()
    def __repr__(self):
        return "<Description object: {}>".format(self.description)

class UserManager(models.Manager):
    def validate(self, request):
        if request.method == "POST":
            valid = True
            for key in request.POST:
                if request.POST[key] == "":
                    valid = False
                    messages.error(request, "{} is required".format(key))
            if len(request.POST["password"]) <= 8:
            	valid= False 
            	messages.error(request, "password must be more than 8 characters")
            if len(request.POST["first_name"]) <=3:
            	valid = False
                messages.error(request, "first name must be more than 3 characters")
            if len(request.POST["last_name"]) <=3:
                valid = False    
            	messages.error(request, "last name must be more than 3 characters")
            if len(request.POST["email"]) <=3:
            	valid = False
            	messages.error(request, "email must be more than 3 characters")	
            if request.POST["password"] != request.POST["confirm_password"]:
                valid = False
                messages.error(request, "password must match confirm password")
            if valid:
                first_name = request.POST["first_name"]
            	last_name = request.POST["last_name"]
            	email = request.POST["email"]
            	password = request.POST["password"]
            	hashed_pw = bcrypt.hashpw(password.encode(),bcrypt.gensalt())
             
                u = User.objects.all()
                #first user becomes userlevel 9 all else 1
                if len(u) < 1:
                    user_level = 9
                else:
                    user_level = 1

                d = Description.objects.create(description="none")

                self.create(first_name=first_name, last_name=last_name, email=email, password=hashed_pw, user_level=user_level, description = d)
                messages.success(request, "Successfully registered!")

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    user_level = models.IntegerField(default=1)
    description = models.OneToOneField(Description)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
    	return "<User object: {} {}>".format(self.first_name,self.email)

    objects = UserManager()



class Message(models.Model): 
    message_content = models.TextField()
    message_creator = models.ForeignKey(User, related_name="createdmessages")
    message_for = models.ForeignKey(User,related_name = "messages")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    comment_creator = models.ForeignKey(User, related_name="createdcomments")
    commented_on = models.ForeignKey(Message, related_name="comments")
    comment_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
