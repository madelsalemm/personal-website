# Generated by Django 4.1.3 on 2022-11-06 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=150)),
                ('image_dicription', models.TextField(max_length=100)),
                ('image_detail', models.TextField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/%y/%m/%d')),
            ],
            options={
                'verbose_name': 'Portfolio',
                'verbose_name_plural': 'Portfolios',
            },
        ),
        migrations.CreateModel(
            name='ProfileImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('pro_image_main', models.ImageField(blank=True, null=True, upload_to='')),
                ('pro_image_sub', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name': 'ProfileImage',
                'verbose_name_plural': 'ProfileImages',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=100)),
                ('degree', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Skills',
            },
        ),
        migrations.RenameField(
            model_name='info',
            old_name='subject',
            new_name='city',
        ),
        migrations.RemoveField(
            model_name='info',
            name='message',
        ),
        migrations.AddField(
            model_name='info',
            name='Freelance',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='info',
            name='age',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='info',
            name='degree',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='info',
            name='phone',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='info',
            name='website',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
