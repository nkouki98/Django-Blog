from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm

# Create your views here.
def register(request):

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base')
    else:
        formObj = CustomUserCreationForm

    return render(request, "users/register.html", {'form': formObj})