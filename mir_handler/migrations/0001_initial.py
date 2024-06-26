# Generated by Django 5.0.6 on 2024-06-01 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MIRFileModel",
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
                ("mir_file", models.FileField(upload_to="mirs/")),
                ("json_file", models.JSONField()),
                ("date_submitted", models.DateField(auto_now_add=True)),
            ],
        ),
    ]
