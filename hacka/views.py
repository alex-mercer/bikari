from django.shortcuts import render


def home(request):
    return render(request,'index.html')


def show_city(request, city):
    pass


def show_event(request, city, event_id):
    pass


def show_user(request, user_name):
    pass
