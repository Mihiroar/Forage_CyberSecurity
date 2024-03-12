from django.db import models

class YourModel(models.Model):
    # Define your fields here
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name
