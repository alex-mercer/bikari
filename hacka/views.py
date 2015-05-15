from django.shortcuts import render, redirect

from .models import *

def register_user(request):
    if request.user.is_authenticated():
        return redirect('/')

    username = request.POST.get('username')
    password = request.POST.get('password')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')

    new_user = HackaUser()
    new_user.user = User.objects.create_user(username=username, password=password, email=email)
    new_user.user.first_name = first_name
    new_user.user.last_name = last_name
    new_user.save()

    return redirect('/')