# Generated by Django 4.2.2 on 2023-06-08 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0008_usergithub'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usergithub',
            name='bio',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='usergithub',
            name='name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
