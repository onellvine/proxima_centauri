from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect

from proxima_exped import models
from .forms import CreateUserForm, LoginUserForm


def usersignup(request):
    # create the user creation form
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('userlogin')
    return render(request, 'users/register.html', {'form': form})


def userlogin(request):
    form = LoginUserForm()

    if request.method == "POST":
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            error = True  # set an error due to authentication errors
            return render(request, 'users/login.html', {'form': form, 'error': error})
        else:
            login(request, user) # login the user to prevent admin changes
            return redirect('home')
    return render(request, 'users/login.html', {'form': form})


def userlogout(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')


def home(request):
    expeditions = models.Expedition.objects.all()[:3]
    return render(request, 'home.html', {'expeditions': expeditions})
