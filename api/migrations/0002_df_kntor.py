# Generated by Django 4.2.7 on 2023-11-27 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="df_kntor",
            fields=[
                (
                    "nop",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
            ],
        ),
    ]
