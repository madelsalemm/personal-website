from django.db import models

# Create your models here.


class Info(models.Model):
    name = models.CharField(max_length = 150)
    age = models.IntegerField(max_length = 2)
    website = models.CharField(max_length = 150)
    degree = models.CharField(max_length = 150)
    phone = models.CharField(max_length = 15)
    city = models.CharField(max_length = 150)
    email =  models.EmailField(max_length = 150)
    Freelance = models.CharField(max_length = 50)
    html = models.IntegerField(max_length = 3)
    css = models.IntegerField(max_length = 3)
    django = models.IntegerField(max_length = 3)
    react = models.IntegerField(max_length = 3)
    api = models.IntegerField(max_length = 3)
    microsoft_project = models.IntegerField(max_length = 3)
    pro_image_main = models.ImageField(upload_to='', null = True , blank=True)
    pro_image_sub = models.ImageField(upload_to='', null = True , blank=True)

    class Meta:
        verbose_name = 'Info'
        verbose_name_plural = 'Infos'
    
    def __str__(self):
        return self.name

class Skill (models.Model):
    skill_name = models.CharField(max_length = 100)
    degree = models.IntegerField(max_length = 3)


    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
    
    def __str__(self):
        return self.skill_name

class ProfileImage (models.Model):
    created_at = models.DateTimeField(auto_now=True)
    
    pro_image_main = models.ImageField(upload_to='', null = True , blank=True)
    pro_image_sub = models.ImageField(upload_to='', null = True , blank=True)

    class Meta:
        verbose_name = 'ProfileImage'
        verbose_name_plural = 'ProfileImages'
    
    def __str__(self):
        return self.created_at

class Portfolio (models.Model):
    
    image_name = models.CharField(max_length = 150)
    image_dicription = models.TextField(max_length = 100)
    image_detail = models.TextField(max_length = 200)
    created_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='media/%y/%m/%d', null = True , blank=True)
    

    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolios'
    
    def __str__(self):
        return self.image_name