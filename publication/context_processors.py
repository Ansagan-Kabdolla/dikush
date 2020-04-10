from .models import Predmeti

def category(request):
    return {"predmeti": Predmeti.objects.all()}