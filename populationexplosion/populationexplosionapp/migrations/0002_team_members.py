# Generated by Django 4.1.5 on 2023-01-24 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('populationexplosionapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='team_members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='photos1')),
                ('name', models.CharField(max_length=250)),
                ('desp', models.TextField()),
            ],
        ),
    ]
