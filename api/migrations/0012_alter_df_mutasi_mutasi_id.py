# Generated by Django 4.2.7 on 2023-11-27 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0011_alter_df_mutasi_bagian_alter_df_mutasi_jabatan_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="df_mutasi",
            name="mutasi_id",
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
