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
    url(r'^updateid/(?P<id>\d+)$', views.updateid),
    url(r'^updatepassword/(?P<id>\d+)$', views.updatepassword),
    url(r'^deleteuser/(?P<id>\d+)$', views.deleteuser), 
    url(r'^removeuser/(?P<id>\d+)$', views.removeuser),
    url(r'^users/show/(?P<id>\d+)$', views.userinfo),
  
]