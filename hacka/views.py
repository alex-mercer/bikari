# coding=utf-8
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from hacka.models import HackaUser, User


def home(request):
    return render(request, 'index.html')


def show_city(request, city):
    pass


def show_event(request, city, event_id):
    pass


def show_user(request, user_name):
    pass


def signup(request):
    if request.user.is_authenticated():
        return redirect(reverse('home'))
    error_message = ''
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')

            new_user = HackaUser()
            new_user.user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name,
                                                     last_name=last_name)
            new_user.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(reverse('home'))
        except:
            error_message = u'ثبت‌نام شما با مشکل مواجه شد. دوباره تلاش کنید.'
    return render(request, 'signup.html', {'error_message': error_message})