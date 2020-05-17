from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    message = models.TextField(max_length=600)

    def __str__(self):
        return self.title