from django.db import models

# Create your models here.
class Student(models.Model):
    roll_no = models.IntegerField()
    mark1 = models.IntegerField()
    mark2 = models.IntegerField()
    mark3 = models.IntegerField()
    passed = models.BooleanField()

    def __str__(self) -> str:
        return str(self.roll_no)
