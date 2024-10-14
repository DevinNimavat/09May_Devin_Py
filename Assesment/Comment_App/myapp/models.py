from django.db import models

# Create your models here.

class CommentData(models.Model):

    DoesNotExist = None
    objects = None
    post_id=models.IntegerField()
    email=models.EmailField()
    name=models.CharField(max_length=200)
    body=models.TextField()
