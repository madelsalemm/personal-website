# Generated by Django 4.1.3 on 2022-11-11 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0014_remove_portfolio_image_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='Portfolio',
            field=models.ManyToManyField(to='contact.portfolio'),
        ),
        migrations.AlterField(
            model_name='info',
            name='skill',
            field=models.ManyToManyField(to='contact.skill'),
        ),
    ]
