# Generated by Django 4.2.2 on 2023-06-08 12:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user_app", "0007_alter_user_gender_alter_user_profile_image_url"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserGithub",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "login",
                    models.CharField(
                        max_length=30,
                        unique=True,
                        validators=[django.core.validators.MinLengthValidator(5)],
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True,
                        max_length=30,
                        null=True,
                        validators=[django.core.validators.MinLengthValidator(3)],
                    ),
                ),
                ("avatar_url", models.CharField(blank=True, max_length=255, null=True)),
                ("company", models.CharField(blank=True, max_length=255, null=True)),
                ("blog", models.URLField(blank=True, max_length=255, null=True)),
                ("location", models.CharField(blank=True, max_length=255, null=True)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                (
                    "bio",
                    models.CharField(
                        blank=True,
                        max_length=30,
                        null=True,
                        validators=[django.core.validators.MinLengthValidator(3)],
                    ),
                ),
                ("public_repos", models.IntegerField(blank=True, null=True)),
                ("followers", models.IntegerField(blank=True, null=True)),
                ("following", models.IntegerField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "User Github",
                "verbose_name_plural": "Users Github",
                "ordering": ("login",),
            },
        ),
    ]
