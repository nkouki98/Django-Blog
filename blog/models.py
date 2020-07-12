from django.db import models
from django.utils import timezone
from users.models import CustomUser
from django.urls import reverse

# Create your models here.



class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(default='default-blog.jpg', upload_to='blog_pics')

    def __str__(self):
        return f'id {self.id} -' + " " + self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})

