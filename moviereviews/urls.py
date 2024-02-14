"""moviereviews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

# Import necessary modules
from django.contrib import admin
from django.urls import path
from movie import views as movieViews

# Define the URL patterns for the application
urlpatterns = [
    # Map the URL '/admin/' to the Django admin interface
    path('admin/', admin.site.urls),
    
    # Map the URL '' (home page) to the home view function in the movieViews module
    path('', movieViews.home),
    
    # Map the URL 'about/' to the about view function in the movieViews module
    path('about/', movieViews.about),
]