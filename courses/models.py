from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Courses(models.Model):
    title = models.CharField(max_length=100)
    times = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(30)])
    complete_times = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(30)])
    def __str__(self):
        return self.title

class Memo(models.Model):
    memo = models.TextField()
    def __str__(self):
        return self.memo