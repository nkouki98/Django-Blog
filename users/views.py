from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as log_in
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('home')
    else:
        form = CustomUserCreationForm()

    context = {'form': form}

    return render(request, "users/register.html", context)


@login_required
def profile(request):
    return render(request, 'users/profile.html')