# coding=utf-8
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib import auth
from hacka.models import HackaUser, User, City, Event


def home(request):
    cities = City.objects.all()
    return render(request, 'home.html', {'auth': request.user.is_authenticated(), 'cities': cities})


def logout(request):
    auth.logout(request)
    return render(request, 'index.html',{'alert_type':'success','alert_message':u'شما با موفقیت خارج شدید'})


def show_city(request, city):
    city = get_object_or_404(City, english_name=city)


def show_event(request, city, event_id):
    city = get_object_or_404(City, english_name=city)
    event = get_object_or_404(Event, id=event_id)
    data = {
        'title': event.title,
        'description': event.description,
        'start': event.start.strftime("%d/%m/%y-%H:%M"),
        'end': event.end.strftime("%d/%m/%y-%H:%M"),
        'tags': [
            e_tag.name for e_tag in event.tags.all()
        ],
        'latitude': event.position.latitude,
        'longitude': event.position.longitude,
        'city': city.english_name
    }
    return render(request, 'event.html', data)


def show_user(request, user_name):
    pass


def signup(request):
    if request.user.is_authenticated():
        return redirect(reverse('home'))
    alert_message = ''
    if request.method == 'POST':
        try:
            password = request.POST.get('password')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            username = email

            new_user = HackaUser()
            new_user.user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name,
                                                     last_name=last_name)
            new_user.save()
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)



            return redirect(reverse('home'))
        except:
            alert_message = u'ثبت‌نام شما با مشکل مواجه شد. دوباره تلاش کنید.'
    return render(request, 'signup.html', {'alert_title': u'اخطار', 'alert_message': alert_message})


def login(request):
    alert_message = ''
    if request.method == 'POST':
        try:
            email = request.POST.get('email')
            password = request.POST.get('password')
            username = email
            user = auth.authenticate(username=username, password=password)

            if user is None:
                alert_message = u'آدرس ایمیل یا رمز عبور نامعتبر می‌باشد.'
            else:
                auth.login(request, user)
                return redirect(reverse('home'))
        except:
            alert_message = u'ورود با مشکل مواجه شد. لطفاً دوباره تلاش کنید'

    return render(request, 'login.html', {'alert_title': u'اخطار', 'alert_message': alert_message})