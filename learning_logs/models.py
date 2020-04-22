from django.db import models

# Create your models here.

class Topic(models.Model):
    text = models.CharField(max_length=200)
    #auto_now_add=True - set this attribute to the current date & time
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text