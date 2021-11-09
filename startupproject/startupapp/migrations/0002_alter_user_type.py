# Generated by Django 3.2.9 on 2021-11-09 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startupapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('US', 'User'), ('MO', 'Moderator'), ('AD', 'Admin')], max_length=128),
        ),
    ]
