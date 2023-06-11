# Generated by Django 4.2.2 on 2023-06-09 18:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user_app", "0012_alter_user_gender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[("Male", "Male"), ("Female", "Female")],
                max_length=13,
                null=True,
            ),
        ),
    ]
