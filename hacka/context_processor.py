from hacka.models import Event, City

def default_context(request):
    return {'events': Event.objects.all(),
            'user': request.user,
            'cities': City.objects.all()
    }