from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import customUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = customUser
        fields = ('email', 'username')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = customUser
        fields = ('email', 'username')