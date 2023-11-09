from django.db import models

# Create your models here.


class Main_contents(models.Model):
    name = models.CharField(max_length=16, unique=True)
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.content
