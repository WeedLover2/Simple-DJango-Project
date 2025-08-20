from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import User
from django.shortcuts import redirect


# Create your views here.

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

def home(request):
    return render(request, 'home.html')

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email, password=password)
            return redirect('home')
        except User.DoesNotExist:
            message = "Invalid email or password"
            return render(request, 'Login.html', {'message': message})
    return render(request, 'Login.html')
