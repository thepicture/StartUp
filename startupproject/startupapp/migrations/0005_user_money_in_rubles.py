# Generated by Django 3.2.9 on 2021-11-10 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startupapp', '0004_startupimage_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='money_in_rubles',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
    ]
