from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import User


# Create your views here.
def FunctionBasedViews(request):
    return HttpResponse("Function Based Views (mambo)")

def user_list_json(request):
    users = list(User.objects.all().values('id', 'first_name', 'last_name', 'gender'))
    return JsonResponse({'users': users})

def user_list(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'user_list.html', context)

def user_conditional_list (request):
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
    return render( request, 'index.html', context)