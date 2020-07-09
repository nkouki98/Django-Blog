from django.http import HttpResponse
from django.shortcuts import redirect




def user_unauthenticated(view_func):
    '''This is a custom decorator which allows to prevent login or register pages to be
    rendered to user if user is authenticated and redirects to preferred url
    '''
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func




