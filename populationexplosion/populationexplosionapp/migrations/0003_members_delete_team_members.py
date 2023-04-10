# Generated by Django 4.1.5 on 2023-01-24 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('populationexplosionapp', '0002_team_members'),
    ]

    operations = [
        migrations.CreateModel(
            name='members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='photos')),
                ('name', models.CharField(max_length=250)),
                ('desp', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='team_members',
        ),
    ]