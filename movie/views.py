# Import necessary modules
from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
# Define the home view function
def home(request):
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    return render(request, 'home.html',{'searchTerm':searchTerm, 'movies': movies})

    

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email':email})

# Define the about view function
def about(request):
    # Return a simple HTTP response with a welcome message
    return HttpResponse('<h1>Welcome to about page<h1>')