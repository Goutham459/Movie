from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView,DeleteView
from django.views.generic.edit import UpdateView
from .models import Movie
from .forms import Movieform

# Create your views here.


def home(request):
    k = Movie.objects.all()
    return render(request, "home.html", {'m': k})

# class MovieList(ListView):
#     model = Movie
#     template_name = "home.html"
#     context_object_name = "m"


def moviedetails(request, p):
    d = Movie.objects.get(id=p)
    return render(request, "moviedetails.html", {'d': d})

# class MovieDetail(DetailView):
#     model = Movie
#     template_name = "moviedetails.html"
#     context_object_name = "d"

def addmovie(request):
    if (request.method == "POST"):
        t = request.POST['t']
        d = request.POST['d']
        y = request.POST['y']
        i = request.FILES['i']
        m = Movie.objects.create(title=t, desc=d, year=y , image=i)
        m.save()
        return home(request)
    return render(request, "addmovie.html" )

# class Movieadd(CreateView):
#     model = Movie
#     template_name = "addmovie.html"
#     fields = '__all__'
#     success_url = reverse_lazy('film:home')


def movieedit(request, p):
    movie = Movie.objects.get(id=id)
    form=MovieForm(instance=movie)
    if request.method == "POST":
        form = Movieform(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return render(request, "moviedetails.html", {'d': movie})
    else:
        form = Movieform(instance=movie)

    return render(request, "editmovie.html", {"form": form})

# class MovieUpdate(UpdateView):
#     model = Movie
#     template_name = "editmovie.html"
#     fields = '__all__'
#     success_url = reverse_lazy('film:home')



def deletemovie(request, p):
    movie = Movie.objects.get(id=p)
    movie.delete()
    return render(request,"home.html") # Redirect to the home page or any other desired page
#
# class MovieDelete(DeleteView):
#     model=Movie
#     success_url=reverse_lazy('film:home')
#     template_name="delete.html"
