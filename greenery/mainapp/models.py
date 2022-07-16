from django.db import models

# Create your models here.

class Greenery(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    photos = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.title



