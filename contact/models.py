from django.db import models

# Create your models here.


class Info(models.Model):
    name = models.CharField(max_length = 150)
    age = models.IntegerField()
    country = models.CharField(max_length = 150)
    degree = models.CharField(max_length = 150)
    phone = models.CharField(max_length = 15)
    city = models.CharField(max_length = 150)
    email =  models.EmailField(max_length = 150)
    Freelance = models.CharField(max_length = 50)
    discription = models.TextField(max_length = 500, null = True , blank=True)
    pro_image_main = models.ImageField(upload_to='media/profile/%y/%m/%d', null = True , blank=True)
    pro_image_sub = models.ImageField(upload_to='media/profile/%y/%m/%d', null = True , blank=True)
    skill = models.ManyToManyField('Skill')
    Portfolio = models.ManyToManyField('Portfolio')
    

    class Meta:
        verbose_name = 'Info'
        verbose_name_plural = 'Infos'
    
    def __str__(self):
        return self.name

class Skill (models.Model):
    person_name = models.ForeignKey(Info, on_delete=models.CASCADE , related_name = 'pesron_info')
    skill_name = models.CharField(max_length = 100)
    degree = models.IntegerField()


    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
    
    def __str__(self):
        return self.skill_name

class Portfolio (models.Model):
    person_name = models.ForeignKey(Info, on_delete=models.CASCADE , related_name = 'pesron_info_image')
    image_name = models.CharField(max_length = 150)
    image_dicription = models.TextField(max_length = 100)
    created_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='media/%y/%m/%d', null = True , blank=True)
    

    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolios'
    def __str__(self):
        return self.image_name
    


