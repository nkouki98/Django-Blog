from django.shortcuts import render
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
# Create your views here.


'''
def home(request):
    """Function based views can be preferred over class-based views
     in certain cases."""
    context = {'posts': Post.objects.all().order_by('-date_posted')}
    return render(request, "blog/home.html", context)
'''

class PostListView(ListView):
    """A better approach is class based views for CRUD applications
    to function based like -> above home(request). Prevents repetitive code, helps with reuseability, structure
    and extendability."""
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']  # '-' for new->old


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):        # searches for post_form template
    model = Post
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)  # run form_valid method on parent class with form as arg


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):  # searches for post_form template
    model = Post
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)  # run form_valid method on parent class with form as arg

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False