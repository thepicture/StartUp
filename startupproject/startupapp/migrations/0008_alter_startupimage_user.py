# Generated by Django 3.2.9 on 2021-11-11 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('startupapp', '0007_alter_startupimage_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startupimage',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='startupapp.user'),
        ),
    ]
