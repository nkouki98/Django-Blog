from django.shortcuts import render
from .models import blogPost

# Create your views here.



def home(request):
    context = {'posts': blogPost.objects.all()}
    return render(request, "blog/home.html", context)