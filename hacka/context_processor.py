from hacka.models import Event

def default_context(request):
    return {'events': Event.objects.all()}