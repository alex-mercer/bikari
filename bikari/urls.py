from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from hacka import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^signup/', views.signup),
    url(r'^login/', views.login),
    url(r'^logout/', views.logout),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<city>\w+)/(?P<event_id>\w+)/$', views.show_event, name='show_event'),
    url(r'^(?P<city>\w+)/', views.show_city, name='show_city'),
    url(r'^/user/(?P<user_name>\w+)/', views.show_user),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
