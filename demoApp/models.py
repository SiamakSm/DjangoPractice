from django.db import models

# Create your models here.

class student(models.Model):
    Name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f"His name is {self.Name} and ({self.age}) years old and his email is {self.email}"
    