"""
URL configuration for movie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import path

from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

app_name = 'film'

urlpatterns = [
    path('', views.home, name="home"),
    # path ('',views.MovieList.as_view(),name="home"),

    path('addmovie', views.addmovie, name="addmovie"),
    # path('addmovie', views.Movieadd.as_view(), name="addmovie"),

    path('moviedetails/<int:p>/', views.moviedetails, name='moviedetails'),
    # path('m/<int:pk>', views.MovieDetail.as_view(), name="moviedetails"),


    path('movieedit/<int:p>', views.movieedit, name="movieedit"),
    # path('movieedit/<int:pk>/', views.MovieUpdate.as_view(), name="movieedit"),

    path('deletemovie/<int:p>', views.deletemovie, name="deletemovie"),
    # path('deletemovie<int:pk>', views.MovieDelete.as_view(), name="deletemovie"),

]




