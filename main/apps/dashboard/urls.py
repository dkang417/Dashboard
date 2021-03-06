from django.conf.urls import url, include
import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^login$', views.login),
	url(r'^process$', views.process),
    url(r'^register$', views.register),
    url(r'^dashboard$', views.dashboard),
    url(r'^logout$', views.logout),
    url(r'^users/new$', views.adduser),
    url(r'^createuser$', views.createuser),
    url(r'^users/edit/(?P<id>\d+)$', views.editid),
    url(r'^users/edit$', views.editprofile),
    url(r'^updatemyprofile$', views.updatemyprofile),
    url(r'^updatemypassword$', views.updatemypassword),
    url(r'^editdescription$', views.editdescription),
    url(r'^updateid/(?P<id>\d+)$', views.updateid),
    url(r'^updatepassword/(?P<id>\d+)$', views.updatepassword),
    url(r'^deleteuser/(?P<id>\d+)$', views.deleteuser), 
    url(r'^removeuser/(?P<id>\d+)$', views.removeuser),
    url(r'^users/show/(?P<id>\d+)$', views.userinfo),
    url(r'^makemessage/(?P<id>\d+)$', views.makemessage),
    url(r'^makecomment/(?P<user_id>\d+)/(?P<message_id>\d+)$', views.makecomment),
     
]