# Generated by Django 4.2.2 on 2023-06-09 00:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user_app", "0010_alter_usergithub_blog"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Male", "Male"),
                    ("Female", "Female"),
                    ("Not Specified", "Not Specified"),
                ],
                max_length=13,
                null=True,
            ),
        ),
    ]
