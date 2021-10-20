from django.shortcuts import render
from .models import Show,Show1,YouTube,YouTubesecond
# Create your views here.

def Home_view(request):
    
    #shows
    shows = Show.objects.latest('updated')
    show1 = Show1.objects.latest('updated')
    #youtbe videos
    youtube = YouTube.objects.latest('updated')
    youtube1= YouTubesecond.objects.latest("updated")

    
    context = {
        'shows':shows,
        'show1':show1,
        'youtube': youtube,
        'youtube1':youtube1
       
       
    }
    return render(request,'index.html', context)


#blog news
def VbuqsNews(request):
    another_context = {}
    
    return render (request, "blog_tour.html", another_context)

def News(request):
    context_again = {}
    
    return render(request, 'Vbuqsnews.html', context_again)