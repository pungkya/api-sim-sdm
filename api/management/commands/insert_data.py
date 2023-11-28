import os
import pandas as pd
from django.core.management.base import BaseCommand
from api.models import *  # Gantilah dengan model Django Anda

class Command(BaseCommand):
    help = 'Insert data from CSV to MySQL database'

    def handle(self, *args, **kwargs):
        csv_file = './df_mutasi_2.csv'  # Ganti dengan path file CSV Anda
        print(os.path.abspath(csv_file))
        if not os.path.exists(csv_file):
            self.stdout.write(self.style.ERROR('File not found.'))
            return

        data_frame = pd.read_csv(csv_file)

        for index, row in data_frame.iterrows():
            df_mutasi.objects.create(
                nippos_id=row['nippos_id'],
                noskep=row['noskep'],
                tgl_skep=row['tgl_skep'],
                tmt=row['tmt'],
                tj=row['tj'],
                jenis_mutasi=row['jenis_mutasi'],
                tgl_brgkt=row['tgl_brgkt'],
                tgl_aktif=row['tgl_aktif'],
                status=row['status'],
                userid=row['userid'],
                tgl_insert=row['tgl_insert'],
                keterangan=row['keterangan'],
                level_jabatan=row['level_jabatan'],
                uid_insert=row['uid_insert'],
                wkt_update=row['wkt_update'],
                uid_update=row['uid_update'],
                rumpun=row['rumpun'],
                tgl_sk=row['tgl_sk'],
                nomor_sk=row['nomor_sk'],
                tmt_sk=row['tmt_sk'],
                rank=row['rank'],
                nopend_asal_id=row['nopend_asal_id'],
                nopend_tujuan_id=row['nopend_tujuan_id'],
                next_tmt=row['next_tmt'],
                rank_jabatan=row['rank_jabatan'],
                durasi_jabatan_sebelumnya=row['durasi_jabatan_sebelumnya'],
                masakerja_jabatan_sebelumnya=row['masakerja_jabatan_sebelumnya'],
                rank_bagian=row['rank_bagian'],
                durasi_bagian_sebelumnya=row['durasi_bagian_sebelumnya'],
                masakerja_bagian_sebelumnya=row['masakerja_bagian_sebelumnya'],
                rank_jabatan_unitkerja=row['rank_jabatan_unitkerja'],
                durasi_jabatan_unitkerja_sebelumnya=row['durasi_jabatan_unitkerja_sebelumnya'],
                masakerja_jabatan_unitkerja_sebelumnya=row['masakerja_jabatan_unitkerja_sebelumnya'],
                rank_bagian_unitkerja=row['rank_bagian_unitkerja'],
                durasi_bagian_unitkerja_sebelumnya=row['durasi_bagian_unitkerja_sebelumnya'],
                masakerja_bagian_unitkerja_sebelumnya=row['masakerja_bagian_unitkerja_sebelumnya'],
                tmt_jabatan=row['tmt_jabatan'],
                tmt_bagian=row['tmt_bagian'],
                tmt_jabatan_unitkerja=row['tmt_jabatan_unitkerja'],
                tmt_bagian_unitkerja=row['tmt_bagian_unitkerja'],
                durasi_jabatan=row['durasi_jabatan'],
                masakerja_jabatan=row['masakerja_jabatan'],
                durasi_bagian=row['durasi_bagian'],
                masakerja_bagian=row['masakerja_bagian'],
                durasi_jabatan_unitkerja=row['durasi_jabatan_unitkerja'],
                masakerja_jabatan_unitkerja=row['masakerja_jabatan_unitkerja'],
                durasi_bagian_unitkerja=row['durasi_bagian_unitkerja'],
                masakerja_bagian_unitkerja=row['masakerja_bagian_unitkerja'],
                posisi_id=row['posisi_id'],
                bagian_id=row['bagian_id'],
                jabatan_id=row['jabatan_id'],
                kategori_durasi_jabatan_sebelumnya_id=row['kategori_durasi_jabatan_sebelumnya_id'],
                kategori_durasi_bagian_sebelumnya_id=row['kategori_durasi_bagian_sebelumnya_id'],
                kategori_durasi_jabatan_unitkerja_sebelumnya_id=row['kategori_durasi_jabatan_unitkerja_sebelumnya_id'],
                kategori_durasi_bagian_unitkerja_sebelumnya_id=row['kategori_durasi_bagian_unitkerja_sebelumnya_id'],
                kategori_durasi_jabatan_id=row['kategori_durasi_jabatan_id'],
                kategori_durasi_bagian_id=row['kategori_durasi_bagian_id'],
                kategori_durasi_jabatan_unitkerja_id=row['kategori_durasi_jabatan_unitkerja_id'],
                kategori_durasi_bagian_unitkerja_id=row['kategori_durasi_jabatan_unitkerja_id'],


                # kategori_durasi_id=row['kategori_durasi_id'],
                # kategori_durasi=row['kategori_durasi'],
                # Tambahkan kolom lain sesuai kebutuhan
            )

        self.stdout.write(self.style.SUCCESS('Data inserted successfully.'))