from django.urls import path
from Musicapp.views import Home_view,VbuqsNews,News
urlpatterns = [
    path('', Home_view, name="home"),
    path('News/', VbuqsNews, name="news"),
    path('Vbuqsnews/', News, name="vbuqsnews"),
]
