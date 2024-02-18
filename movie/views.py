# Import necessary modules
from django.shortcuts import render
from django.http import HttpResponse

# Define the home view function
def home(request):
    # Get the search term from the query parameters
    searchTerm = request.GET.get('searchMovie')
    
    # Render the home.html template with the search term as a context variable
    return render(request, 'home.html', {'searchTerm' : searchTerm})

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email':email})

# Define the about view function
def about(request):
    # Return a simple HTTP response with a welcome message
    return HttpResponse('<h1>Welcome to about page<h1>')