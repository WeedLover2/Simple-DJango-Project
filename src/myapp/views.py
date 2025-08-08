from django.http import HttpResponse as HTTPResponse
from django.http import JsonResponse as JsonResponse
from .models import User
from django.shortcuts import render

# Create your views here.
def FunctionBasedViews(request):
    return HTTPResponse("Function Based Views (mambo)")

def user_list_json(request):
    # Mengambil semua user dari database sebagai list of dict
    users = list(User.objects.all().values('id', 'first_name', 'last_name', 'gender'))
    return JsonResponse({'users': users})

def index(request):
    Student = {'Malik', 'Tian', 'Adit', 'Rifqi', 'Rehan'}
    return render(request, 'index.html', {'Student': Student})


