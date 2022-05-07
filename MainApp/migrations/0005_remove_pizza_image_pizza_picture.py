# Generated by Django 4.0.4 on 2022-05-07 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0004_pizza_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='image',
        ),
        migrations.AddField(
            model_name='pizza',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
    ]