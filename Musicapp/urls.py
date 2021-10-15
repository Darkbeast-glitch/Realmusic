from django.urls import path
from Musicapp.views import Home_view
urlpatterns = [
    path('', Home_view, name="home")
]
