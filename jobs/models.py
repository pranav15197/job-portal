from django.db import models
from django.contrib.auth.models import User


class Job(models.Model):
    position_name = models.CharField(max_length=100)
    text_description = models.TextField()
    min_age = models.IntegerField()
    max_age = models.IntegerField()
    salary = models.IntegerField()
    n_openings = models.IntegerField()
    creater = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.position_name
