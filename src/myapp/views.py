from django.http import HttpResponse, JsonResponse, HttpResponseForbidden
from django.shortcuts import render
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm




# Create your views here.

# lOGIN
def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user) 
            return redirect('home')
        else:
            message = "Invalid email or password"
            return render(request, 'Login.html', {'message': message})
    return render(request, 'Login.html')

# REGISTER
def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# LOGOUT
def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

def custom_protected_view(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden("You must login first to see this content")
    return render(request, 'protected.html')
    
@login_required
def userList (request):
    all_users = User.objects.all()
    male_users = User.objects.filter(gender='M')
    female_users = User.objects.filter(gender='F')
    context = {
        'all_users': all_users,
        'male_users': male_users,
        'female_users': female_users,
        'total_users': all_users.count(),
        'male_count': male_users.count(),
        'female_count': female_users.count(),
        'has_users': all_users.exists(),
    }
    return render( request, 'user.html', context)

@login_required
def home(request):
    return render(request, 'home.html')

