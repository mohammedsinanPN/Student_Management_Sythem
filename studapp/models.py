from django.db import models

class StudentDb(models.Model):

    name = models.CharField(max_length=100)
    roll_number = models.IntegerField()
    course = models.CharField(max_length=100)
    age = models.IntegerField()
    place = models.CharField(max_length=100)

    def __str__(self):
        return self.name