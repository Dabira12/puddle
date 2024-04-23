from django.shortcuts import render
from wager.models import Sport, Wager
# Create your views here.
def index(request):
    wagers = Wager.objects.all()
    return render(request, 'core/index.html',{'wagers':wagers})