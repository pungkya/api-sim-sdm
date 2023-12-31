# Generated by Django 4.2.7 on 2023-11-27 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_df_sdm"),
    ]

    operations = [
        migrations.AddField(
            model_name="df_sdm",
            name="kode_jiwa",
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name="df_sdm",
            name="masih_hidup",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="df_sdm",
            name="sudah_berhenti",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="df_sdm",
            name="usia",
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="df_sdm",
            name="status_transfer",
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name="df_sdm",
            name="tempat_lahir",
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name="df_sdm",
            name="tgl_berhenti",
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name="df_sdm",
            name="tgl_disumpah",
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name="df_sdm",
            name="tgl_kerja",
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name="df_sdm",
            name="tgl_meninggal",
            field=models.DateTimeField(),
        ),
    ]
