from django.db import models


class Main_contents(models.Model):
    name = models.CharField(max_length=16, unique=True)
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title


class Department(models.Model):
    name = models.CharField(max_length=64, unique=True)
    title = models.CharField(max_length=255, )
    description = models.TextField()

    def __str__(self):
        return self.title
