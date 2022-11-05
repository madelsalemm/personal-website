from django.db import models

# Create your models here.


class Info(models.Model):
    name = models.CharField(max_length = 150)
    email = models.EmailField(max_length = 150)
    subject = models.CharField(max_length = 150)
    message = models.CharField(max_length = 300)
    
    class Meta:
        verbose_name = 'Info'
        verbose_name_plural = 'Infos'
    
    def __str__(self):
        return self.name