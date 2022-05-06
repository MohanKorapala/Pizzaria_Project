# Generated by Django 3.0.5 on 2022-05-05 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0002_topping'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.Pizza')),
            ],
        ),
    ]
