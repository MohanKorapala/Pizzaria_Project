from distutils.command.upload import upload
from django.db import models

# Create your models here. TABLES   
class Pizza(models.Model):
    text = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.text 

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping_name = models.TextField()


    def __str__(self):
        return self.topping_name

class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    text = models.TextField()


    def __str__(self):
        return self.text