# Generated by Django 4.1.3 on 2022-11-11 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0015_alter_info_portfolio_alter_info_skill'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='website',
            new_name='country',
        ),
    ]
