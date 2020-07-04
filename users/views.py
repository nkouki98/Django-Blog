from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm
from .decorators import user_unauthenticated
from .models import CustomUser, Profile
from blog.models import Post

# Create your views here.

@user_unauthenticated
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for ' + username )
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, "users/register.html", context)



@user_unauthenticated
def login(request):
    return render(request, "users/login.html")



@login_required
def profile(request):
     if request.method == 'POST':
         form_u = UserUpdateForm(request.POST, instance=request.user)
         form_p = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
         if form_u.is_valid() and form_p.is_valid():
             form_u.save()
             form_p.save()
             messages.success(request, f'Profile successfully updated!')
             return redirect('profile')
     else:
         form_u = UserUpdateForm(instance=request.user)
         form_p = ProfileUpdateForm(instance=request.user.profile)
     context = {'form_u': form_u, 'form_p':form_p}
     return render(request, 'users/profile.html', context)



@login_required
def displayProfile(request, username):
    user = CustomUser.objects.get(username=username)
    return render(request, 'users/userprofile.html', {'posts': Post.objects.filter(author=user), 'user': user})


