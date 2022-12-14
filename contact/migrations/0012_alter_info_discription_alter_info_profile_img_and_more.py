# Generated by Django 4.1.3 on 2022-11-11 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0011_info_discription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='discription',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='profile_img',
            field=models.ManyToManyField(blank=True, null=True, to='contact.profileimage'),
        ),
        migrations.AlterField(
            model_name='info',
            name='skill',
            field=models.ManyToManyField(blank=True, null=True, to='contact.skill'),
        ),
    ]
