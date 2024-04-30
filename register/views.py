from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CustomUser
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, "users/login.html")


def register(request):
    return render(request, "users/register.html")

@csrf_exempt
def add_user(request):
    if request.method == 'POST':
        # Extract form data
        first_name = request.POST.get('first_name')
        print(first_name)
        last_name = request.POST.get('last_name')
        print(last_name)
        email = request.POST.get('email')
        print(email)
        password = request.POST.get('password')
        print(password)
        mobile_no = request.POST.get('mobile_no')
        print(mobile_no)
        # Hash the password
        hashed_password = make_password(password)
        CustomUser.objects.create(first_name=first_name, last_name=last_name, email=email, password=hashed_password, mobile_number=mobile_no, is_admin=False)
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print(email)
        password = request.POST.get('password')
        print(password)
         # Authenticate user
        user = authenticate(request, email=email, password=password)

        if user is not None:
            # User is authenticated, log in the user
            login(request, user)
            return JsonResponse({'status': 'success', 'message': 'Login successful'})
        else:
            # Authentication failed, return error message
            return JsonResponse({'status': 'error', 'message': 'Invalid email or password'})
    else:
        # Handle other HTTP methods if necessary
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

@login_required
def dashboard(request):
    try:
        pass
    except Exception as e:
        print(e)
    return render(request, "base/base.html")