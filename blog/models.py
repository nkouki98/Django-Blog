from django.db import models
from django.utils import timezone
from users.models import customUser
# Create your models here.



class blogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(customUser, on_delete=models.CASCADE)



    def __str__(self):
        return self.title


