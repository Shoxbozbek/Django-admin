from django.db import models

class Home(models.Model):
    
    logo = models.CharField(max_length=40)
    login = models.CharField(max_length=20)


    def __str__(self):
        return self.logo
