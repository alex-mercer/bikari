# coding=utf-8
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib import auth
from hacka.models import HackaUser, User, City, Event, Registration


def home(request):
    cities = City.objects.all()
    return render(request, 'home.html', {'auth': request.user.is_authenticated(), 'cities': cities})


def logout(request):
    auth.logout(request)
    return render(request, 'index.html', {'alert_type': 'success', 'alert_message': u'شما با موفقیت خارج شدید'})


def show_city(request, city):
    city = get_object_or_404(City, english_name=city)
    events = Event.objects.filter(city=city).order_by('start')
    return render(request, 'city.html',{'city': city, 'events': events})


def show_event(request, city, event_id):
    city = get_object_or_404(City, english_name=city)
    event = get_object_or_404(Event, id=event_id)
    if request.POST:
        if not request.user.is_authenticated():
            return render(request, 'event.html', {'event': event, 'city': city,
                      'alert_type': 'error', 'alert_message': u'برای ثبت نام ابتدا باید وارد شوید.'})
        else:
            if Registration.objects.filter(user=request.user, event=event).count():
                return render(request, 'event.html', {'event': event, 'city': city,
                          'alert_type': 'error', 'alert_message': u'شما قبلا برای ثبت نام اقدام کردید.'})
            user = request.user.hackauser
            new_reg = Registration(user=request.user, event=event, status='P')
            new_reg.save()
            return render(request, 'events.html', {'user': user,
                        'events': Registration.objects.filter(user_id=user.id),
                        'alert_type': 'success', 'alert_message': u'ثبت نام شما با موفقیت انجام شد.'})
    return render(request, 'event.html', {'event': event, 'city': city})


@login_required
def show_user(request):
    user = request.user.hackauser
    return render(request, 'events.html', {'user': user, 'events': Registration.objects.filter(user_id=user.id)})


def signup(request):
    if request.user.is_authenticated():
        return redirect(reverse('home'))
    alert_message = ''
    try:
        if request.method == 'POST':
            password = request.POST.get('password')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            username = email

            new_user = HackaUser()
            new_user.user = User.objects.create_user(username=username, password=password, email=email,
                                                     first_name=first_name, last_name=last_name)
            new_user.save()

            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)

            user.email_user(subject='تایید ثبت نام', message='ثبت نام شما با موفقیت انجام شد')

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


def edit_profile(request):
    if not request.user.is_authenticated():
        return redirect(reverse('login'))

    context = {}

    if request.method == "POST":
        password = ''
        username = request.user.username
        changed = False
        if request.POST.get('first_name'):
            request.user.first_name = request.POST.get('first_name')
            changed = True
        if request.POST.get('last_name'):
            request.user.last_name = request.POST.get('last_name')
            changed = True
        if request.POST.get('new_password'):
            if request.user.check_password(request.POST.get('password')):
                request.user.set_password(request.POST.get('new_password'))
            else:
                context['alert_title'] = u'خطا در انجام تغییرات'
                context['alert_message'] = u'رمز عبور شما نامعتبر است'
                return render(request, 'edit_profile.html', context)
            password = request.POST.get('new_password')
            changed = True
        request.user.save()
        if password:
            request.user = auth.authenticate(username=username, password=password)
            auth.login(request, request.user)
        if changed:
            context['alert_title'] = u'تغییر اطلاعات'
            context['alert_message'] = u'اطلاعات شما با موفقیت به روز شد'
            context['alert_type'] = 'success'


    context['user'] = request.user

    return render(request, 'edit_profile.html', context)
