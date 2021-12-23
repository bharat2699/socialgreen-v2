from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Leaf(models.Model):
    body = models.CharField(max_length=250)
    created_by = models.ForeignKey(
        User, related_name='leafs', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at', )


class Like(models.Model):
    leaf = models.ForeignKey(Leaf, related_name='likes', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
