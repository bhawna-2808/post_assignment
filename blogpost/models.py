from django.db import models
from register.models import CustomUser

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    published = models.BooleanField(default=False)
    published_date = models.DateTimeField(auto_now_add=True)

