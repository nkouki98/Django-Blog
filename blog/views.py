from django.shortcuts import render
from .models import Post
from django.views.generic import ListView
# Create your views here.


'''
def home(request):
    """Function based views can be preferred over class-based views
     in certain cases."""
    context = {'posts': Post.objects.all().order_by('-date_posted')}
    return render(request, "blog/home.html", context)
'''

class PostlistView(ListView):
    """A better approach is class based views for CRUD applications
    to function based like -> above home(request). Prevents repetitive code, helps with reuseability, structure
    and extendability."""
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']  # '-' for new->old


