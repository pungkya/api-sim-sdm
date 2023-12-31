# Generated by Django 4.2.7 on 2023-11-27 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_df_kntor"),
    ]

    operations = [
        migrations.CreateModel(
            name="df_kantor",
            fields=[
                (
                    "nopend",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("nama_kantor", models.TextField()),
                ("kode_level", models.BigIntegerField()),
                ("singkatan_kelas_kantor", models.TextField()),
                ("jenis_relasi", models.TextField()),
                ("status_aktif", models.TextField()),
                ("kprk", models.TextField()),
                ("kcu", models.TextField()),
                (
                    "kelas_kantor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.df_kelas_kantor",
                    ),
                ),
                (
                    "regional",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.df_regional",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="df_kntor",
        ),
    ]
