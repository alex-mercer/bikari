from django.conf.urls import patterns, include, url
from django.contrib import admin
from hacka import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^signup/', views.signup),
    url(r'^(?P<city>\w+)/', views.show_city),
    url(r'^/user/(?P<user_name>\w+)/', views.show_user),
    url(r'^/(?P<city>\w+)/(?P<event_id>\w+)/', views.show_event,name='show_event'),



    url(r'^admin/', include(admin.site.urls)),
)
