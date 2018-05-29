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

    def validateUserInfo(self,request,id):
        if request.method == "POST":
            valid = True
            for key in request.POST:
                if request.POST[key] == "":
                    valid = False
                    messages.error(request, "{} is required".format(key))
            if len(request.POST["first_name"]) <=3:
                valid = False
                messages.error(request, "first name must be more than 3 characters")
            if len(request.POST["last_name"]) <=3:
                valid = False    
                messages.error(request, "last name must be more than 3 characters")
            if len(request.POST["email"]) <=3:
                valid = False
                messages.error(request, "email must be more than 3 characters")
            if valid:
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

    def validatePassword(self,request,id):

         if request.method == "POST":
            valid = True
            for key in request.POST:
                if request.POST[key] == "":
                    valid = False
                    messages.error(request, "{} is required".format(key))

            if len(request.POST["password"]) <= 8:
                valid= False 
                messages.error(request, "password must be more than 8 characters")
            if request.POST["password"] != request.POST["confirm_password"]:
                valid = False
                messages.error(request, "password must match confirm password") 
            if valid:
                user = User.objects.get(id=id)
                password = request.POST["password"]
                confirm = request.POST["confirm_password"]
                hashed_pw = bcrypt.hashpw(password.encode(),bcrypt.gensalt())

                user.password = hashed_pw
                user.save()
                messages.success(request,"password successfully updated")

    def validateMyinfo(self,request):
        if request.method == "POST":
            valid = True
            for key in request.POST:
                if request.POST[key] == "":
                    valid = False
                    messages.error(request, "{} is required".format(key))
            if len(request.POST["first_name"]) <=3:
                valid = False
                messages.error(request, "first name must be more than 3 characters")
            if len(request.POST["last_name"]) <=3:
                valid = False    
                messages.error(request, "last name must be more than 3 characters")
            if len(request.POST["email"]) <=3:
                valid = False
                messages.error(request, "email must be more than 3 characters")
            if valid:
                user = User.objects.get(id=request.session['id'])
                first_name = request.POST["first_name"]
                last_name = request.POST["last_name"]
                email = request.POST["email"]
               
                

                user.first_name = first_name
                user.last_name = last_name
                user.email = email 
                user.save()
                messages.success(request,"profile successfully updated")

    def validateMypassword(self,request):
         if request.method == "POST":
            valid = True
            for key in request.POST:
                if request.POST[key] == "":
                    valid = False
                    messages.error(request, "{} is required".format(key))

            if len(request.POST["password"]) <= 8:
                valid= False 
                messages.error(request, "password must be more than 8 characters")
            if request.POST["password"] != request.POST["confirm_password"]:
                valid = False
                messages.error(request, "password must match confirm password") 
            if valid:
                user = User.objects.get(id=request.session['id'])
                password = request.POST["password"]
                confirm = request.POST["confirm_password"]
                hashed_pw = bcrypt.hashpw(password.encode(),bcrypt.gensalt())

                user.password = hashed_pw
                user.save()
                messages.success(request,"password successfully updated")

    def validateDescription(self,request): 
        if request.method == "POST":
            valid = True  
            if len(request.POST["description"]) <= 1:
                valid= False 
                messages.error(request, "Description must be more than 1 character") 
            if valid: 
                user = User.objects.get(id=request.session['id'])
                description= request.POST["description"]
                user.description.description = description
                user.description.save()
                messages.success(request,"description successfully updated") 

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



class MessageManager(models.Manager):
    def validateMessage(self, request, id):
        if request.method == "POST":
            valid = True
            if len(request.POST["add_message"]) <=1:
                valid = False
                messages.error(request, "message must be more than 1 character")        
            if valid:
                user = User.objects.get(id=id)
                message_creator = User.objects.get(id=request.session['id'])
                message_content = request.POST["add_message"]
                Message.objects.create(message_content=message_content, message_creator= message_creator, message_for = user)
                messages.success(request,"message successfully updated")

class Message(models.Model): 
    message_content = models.TextField()
    message_creator = models.ForeignKey(User, related_name="createdmessages")
    message_for = models.ForeignKey(User,related_name = "messages")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MessageManager()

class CommentManager(models.Manager):
    def validateComment(self,request,user_id,message_id):
        if request.method == "POST":
            valid = True
            if len(request.POST["add_comment"]) <=1:
                valid = False
                messages.error(request, "comment must be more than 1 character")
            if valid:
                message = Message.objects.get(id=message_id)
                comment_creator = User.objects.get(id=request.session['id'])
                comment_content = request.POST["add_comment"]
                Comment.objects.create(comment_creator = comment_creator, comment_content= comment_content, commented_on = message)
                messages.success(request,"comment successfully updated")

class Comment(models.Model):
    comment_creator = models.ForeignKey(User, related_name="createdcomments")
    commented_on = models.ForeignKey(Message, related_name="comments")
    comment_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()
