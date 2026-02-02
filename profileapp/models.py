from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    bio = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    resume = models.FileField(upload_to="resumes/", blank=True)
    image = models.ImageField(upload_to="profile/", blank=True)

    def __str__(self):
        return self.name
