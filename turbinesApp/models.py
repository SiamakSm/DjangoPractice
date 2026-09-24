from django.db import models

# Create your models here.

class Turbine(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Alert(models.Model):
    turbine = models.ForeignKey(Turbine, on_delete=models.CASCADE)
    message = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.turbine.name}] {self.message}"
        