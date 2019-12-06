from django.db import models



class Post (models.Model):
    images = models.ImageField(upload_to='pics')
    offers = models.BooleanField()
    head = models.CharField(max_length=133)
    descrption = models.CharField(max_length=150)
    amount = models.IntegerField()
class blog (models.Model):
    images = models.ImageField(upload_to='pics')
    date = models.DateField()
    head = models.CharField(max_length=133)
    description = models.CharField(max_length=150)

class enquery (models.Model):
     name = models.CharField(max_length=150)
     email = models.EmailField()
     subject = models.CharField(max_length=150)
     message = models.CharField(max_length=150)
