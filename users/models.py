from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from PIL import Image
# Create your models here.

class CustomUserManager(BaseUserManager):

     def create_user(self, email, username, password=None):
         if not email:
             raise ValueError("Users must have an email address")
         if not username:
             raise ValueError("Username is required")

         user = self.model(
             email=self.normalize_email(email),
             username=username,
         )
         user.set_password(password)
         user.save(using=self._db)
         return user

     def create_superuser(self, email, username, password):
         user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
         user.is_admin=True
         user.is_staff=True
         user.is_superuser=True
         user.save(using=self._db)
         return user


class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(verbose_name="email", max_length=100, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email





class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')


    def __str__(self):
        return f'{self.user.username}'


    #override save method
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)