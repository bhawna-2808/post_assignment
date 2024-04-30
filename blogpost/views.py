from django.shortcuts import render
from .models import *
from django.db.models import Q
from .forms import *
import requests
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, ListCreateAPIView


admin_posts = Post.objects.filter(
    Q(author__is_admin=True) & Q(author__email='admin') & Q(published=True)
)

# queryset

def view_post(request):
    admin_posts = Post.objects.filter(
    Q(author__is_admin=True) & Q(author__email='admin') & Q(published=True)
)
   
def createform(request, pk=None, is_delete=0):
    form = PostForm(request.POST or None)
    message = "Post Added Successfully !!"
    if pk is not None and is_delete == 0:
        createid_ins = Post.objects.get(pk=pk)
        form = PostForm(
            request.POST or None, instance=createid_ins
        )
        message = "Post Updated Successfully !!"
    elif pk is not None and is_delete != 0:
        Post.objects.filter(pk=pk).delete()
        message = "Post Deleted Successfully !!"
        # messages.success(request, message)
        return redirect("post-list")
    if form.is_valid():
        form.save()
        # messages.success(request, message)
        return redirect("post-list")

    context = {
        "form": form,
    }
    return render(request, "post/add_post.html", context)  



def get_weather(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            # Extracting relevant weather information
            weather_main = data['weather'][0]['main']
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            
            # Printing the weather information
            print(f"Weather in {city_name}:")
            print(f" - Main: {weather_main}")
            print(f" - Description: {weather_description}")
            print(f" - Temperature: {temperature}°C")
            print(f" - Humidity: {humidity}%")
            print(f" - Wind Speed: {wind_speed} m/s")
        else:
            print(f"Failed to fetch weather data. Error {response.status_code}: {data['message']}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
city_name = "New York"
api_key = "YOUR_API_KEY"  # Replace this with your actual API key from OpenWeatherMap
get_weather(city_name, api_key)


""" APIS Of list and create post
"""
class PostAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer