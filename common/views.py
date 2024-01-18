from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from .models import User
from .forms import UserForm

# Create your views here.
def index(request):
    return render(request, 'common/index.html')

def signup(request):
    if (request.method == 'POST'):
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            login(request, user)
            return redirect('/')
    else:
        user_form = UserForm()
    return render(request, 'common/signup.html', {'user_form': user_form})

def logout_page(request):
    logout(request)
    return redirect('/')
