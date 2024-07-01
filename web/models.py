from django.db import models

# Create your models here.

class newsflash (models.Model):
    news = models.CharField(max_length=255)

    def __str__(self):
        return self.news
    
    