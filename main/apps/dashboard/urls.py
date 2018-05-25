from django.conf.urls import url, include
import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^login$', views.login),
	url(r'^process$', views.process),
    url(r'^register$', views.register),
    url(r'^dashboard$', views.dashboard),
    url(r'^logout$', views.logout)
    # url(r'^main$', views.index),
    # url(r'^register$', views.register),
    # url(r'^login$', views.login),
    # url(r'^travels$', views.travels),
    # url(r'^logout$', views.logout),
    # url(r'^travels/add$', views.add),
    # url(r'^addtrip$', views.addtrip),
    # url(r'^join/(?P<id>\d+)$', views.join),
    # url(r'^travels/destination/(?P<id>\d+)$', views.showtrip)
]