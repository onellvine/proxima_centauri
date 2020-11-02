from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect, get_object_or_404

from proxima_exped import models
from proxima_exped.models import Expedition
from .forms import CreateUserForm, LoginUserForm

from .models import Reviews


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


def addreview(request):
    "Take the review filled in by the user and add to the database."
    if request.user.is_authenticated:  # get the authenticated user
        user = request.user

    if request.method == "POST":  
        # get the review posted in the textarea, and the corresponding object
        comment = request.POST['review']
        exped_id = request.POST['expedition-id']

    expedition = get_object_or_404(Expedition, pk=exped_id)  # get the current instance of expedition object

    review = Reviews(comment=comment, expedition=expedition, user=user)
    review.save()

    return redirect('home')


def home(request):
    expeditions = models.Expedition.objects.all()[:3]
    reviews = Reviews.objects.all()[:3]
    return render(request, 'home.html', {'expeditions': expeditions, 'reviews': reviews})
