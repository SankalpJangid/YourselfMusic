# Generated by Django 3.0.3 on 2021-02-17 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YourMusic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='statusinfo',
            name='cover_image',
            field=models.ImageField(blank=True, default='1.jpg', null=True, upload_to='cover_image'),
        ),
    ]
