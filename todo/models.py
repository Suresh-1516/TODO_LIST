from django.db import models

class Notes(models.Model):

    content = models.CharField(max_length=100,default=None)
    date = models.DateField(auto_now_add=True)
