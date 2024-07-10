from django.db import models

class NewSite(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    author = models.CharField(max_length=40)
    datetime = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title