# Generated by Django 4.2.2 on 2023-06-07 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0006_alter_user_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_image_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]