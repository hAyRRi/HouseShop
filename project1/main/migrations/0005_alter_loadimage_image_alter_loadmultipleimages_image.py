# Generated by Django 4.1.3 on 2022-12-02 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_loadmultipleimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loadimage',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='loadmultipleimages',
            name='image',
            field=models.FileField(upload_to='img'),
        ),
    ]