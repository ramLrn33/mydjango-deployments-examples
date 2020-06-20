from django.db import models

# Create your models here.
class people(models.Model):
    FirstName=models.CharField(max_length=264)
    LastName=models.CharField(max_length=264)
    Email=models.EmailField(max_length=264)
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.Email
