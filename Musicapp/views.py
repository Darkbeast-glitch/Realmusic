from django.shortcuts import render
from .models import Show,Show1,BigHitters
# Create your views here.

def Home_view(request):
    
    #shows
    shows = Show.objects.latest('updated')
    show1 = Show1.objects.latest('updated')
    bighitters = BigHitters.objects.latest('updated')
    
    context = {
        'shows':shows,
        'show1':show1,
        'bighitters':bighitters,
       
    }
    return render(request,'index.html', context)