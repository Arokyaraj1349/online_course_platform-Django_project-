from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=50)
    description= models.TextField()
    price=models.IntegerField(default=0)
    image = models.ImageField(upload_to='course_images/', null=True, blank=True)

    