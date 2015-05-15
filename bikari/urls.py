from django.conf.urls import patterns, include, url
from django.contrib import admin
from hacka import views

urlpatterns = patterns('',
    url(r'^$', views.home),
    url(r'^(?P<city>.+)/', views.show_city),
    url(r'^/(?P<city>.+)/(?P<event_id>.+)/', views.show_event),
    url(r'^/user/(?P<user_name>.+)/', views.show_user),


    url(r'^admin/', include(admin.site.urls)),
)
