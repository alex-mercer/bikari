from django.conf.urls import patterns, include, url
from django.contrib import admin
from hacka import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', views.show_user),
    url(r'^(?P<city>\w+)/(?P<event_id>\w+)/$', views.show_event, name='show_event'),
    url(r'^(?P<city>\w+)/$', views.show_city, name='show_city'),

    url(r'^edit_profile$', views.edit_profile, name='edit_profile'),
)
