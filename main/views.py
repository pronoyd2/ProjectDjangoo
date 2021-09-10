from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth import authenticate
from django.db.models import Avg, query
from django.db.models import aggregates

# Create your views here.
def home(request):
    query = request.GET.get("title")
    allMovies = None
    if query:
        allMovies= Movie.objects.filter(name__icontains=query)
    else:
        allMovies = Movie.objects.all()

    context = {
    "movies": allMovies,
    }   
    return render(request, 'main\index.html', context)
def detail(request, id):
        movie = Movie.objects.get(id=id)
        reviews= Review.objects.filter(movie=id).order_by("-comment")
        average= reviews.aggregate(Avg("rating"))["rating__avg"]
        
        if average == None:
            average = 0
        average = round (average, 2)

        context = {
            "movie": movie,
            "reviews": reviews,
            "average": average
            
        }
        return render(request, 'main/details.html', context)
def add_movies(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == "POST":
                form = Movieform(request.POST or None)

                if form.is_valid():
                    data = form.save(commit=False)
                    data.save()
                    return redirect ("main:home")
            else:
                    form = Movieform()
            return render(request, 'main/addmovies.html', {'form': form, "controller": "Add Movies"})
        else:
            return redirect("main:home")
    return redirect("accounts:login")
#editMovies
def edit_movies(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            movie = Movie.objects.get(id=id)
        if request.method== 'POST':
            form = Movieform(request.POST or None, instance= movie)
            if form.is_valid():
                data= form.save(commit=False)
                data.save()
                return redirect("main:detail", id)
        else:
            form= Movieform(instance= movie)
        return render(request, 'main/addmovies.html', {"form" : form, "controller": "Edit Movies"}) 
def delete_movies(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect("main:home")
    return redirect("accounts:login")
def add_review (request, id):
    if request.user.is_authenticated:
        movie= Movie.objects.get(id=id)
        if request.method == "POST":
            form = Reviewform(request.POST or None)
            if form.is_valid():
                data = form.save(commit=False)
                data.comment = request.POST["comment"]
                data.rating = request.POST["rating"]
                data.user = request.user
                data.movie = movie
                data.save()
                return redirect("main:detail", id)
        else:
            form = Reviewform()
        return render (request, 'main/details.html', {"form": form})
    else:
        return redirect("accounts:login")
def edit_review(request, movie_id, review_id):
    if request.user.is_authenticated:
        movie = Movie.objects.get(id = movie_id)
        review= Review.objects.get(movie= movie, id= review_id)
        if request.user == review.user:
            if request.method == "POST":
                form = Reviewform(request.POST, instance = review)
                if form.is_valid():
                    data = form.save(commit=False)
                    data.save()
                    return redirect ("main:detail", movie_id)
            else:
                form = Reviewform(instance=review)   #Itshould return if not else one
            return render(request, 'main/editreview.html', {"form": form})
        else:
            return redirect("main:detail", movie_id)
    else:
        return redirect("accounts:login")


def delete_review(request, movie_id, review_id):
    if request.user.is_authenticated:
        movie = Movie.objects.get(id = movie_id)
        review= Review.objects.get(id= review_id)
        if request.user == review.user:
            review.delete()
        return redirect('main:detail', movie_id)
    else:
        return redirect ('accounts:login')






        
