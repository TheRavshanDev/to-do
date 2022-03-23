from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    body = models.TextField(max_length=2000, blank=True)
    date = models.DateTimeField(blank=True, null=True)
    photo = models.FileField(upload_to='images/',null=True, blank=True)

    def __str__(self):
        return self.title