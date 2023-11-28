from django.db import models
import MySQLdb
import pymysql
pymysql.install_as_MySQLdb()


# Create your models here.
class df_regional(models.Model):
    regional_id = models.BigAutoField(primary_key=True)
    regional = models.TextField()

class df_agama(models.Model):
    agama_id = models.BigAutoField(primary_key=True)
    agama = models.TextField()

class df_jabatan(models.Model):
    jabatan_id = models.BigAutoField(primary_key=True)
    jabatan = models.TextField()

class df_kelas_kantor(models.Model):
    kelas_kantor_id = models.BigAutoField(primary_key=True)
    kelas_kantor = models.TextField()

class df_posisi(models.Model):
    posisi_id = models.BigAutoField(primary_key=True)
    posisi = models.TextField()

class df_status_pegawai(models.Model):
    status_pegawai_id = models.BigAutoField(primary_key=True)
    status_pegawai = models.TextField()

class df_status_kerja(models.Model):
    status_kerja_id = models.BigAutoField(primary_key=True)
    status_kerja = models.TextField()

class df_bagian(models.Model):
    bagian_id = models.BigAutoField(primary_key=True)
    bagian = models.TextField()
    status_bagian = models.TextField()

class df_status_nikah(models.Model):
    status_nikah_id = models.BigAutoField(primary_key=True)
    status_nikah = models.TextField()

class df_kategori_durasi(models.Model):
    kategori_durasi_id = models.BigAutoField(primary_key=True)
    kategori_durasi = models.TextField()
    
class df_kantor(models.Model):
    nopend = models.CharField(max_length=20, primary_key = True)
    nama_kantor = models.TextField()
    kode_level = models.BigIntegerField()
    singkatan_kelas_kantor = models.TextField()
    jenis_relasi = models.TextField()
    status_aktif = models.TextField()
    kprk = models.TextField()
    kcu = models.TextField()
    kelas_kantor = models.ForeignKey(df_kelas_kantor, on_delete= models.CASCADE)
    regional = models.ForeignKey(df_regional, on_delete= models.CASCADE)    

class df_sdm(models.Model):
    nippos = models.BigIntegerField(primary_key=True)
    nama = models.TextField()
    tgl_lahir = models.TextField()
    tempat_lahir = models.TextField()
    total_grade = models.TextField()
    suskel = models.TextField()
    jenis_kelamin = models.TextField()
    tgl_meninggal = models.TextField()
    tgl_disumpah = models.TextField()
    tgl_kerja = models.TextField()
    tgl_berhenti = models.TextField()
    golongan_darah = models.TextField()
    alamat = models.TextField()
    kota = models.TextField()
    kodepos = models.TextField()
    telp = models.TextField()
    no_urut = models.TextField()
    status = models.TextField()
    passs = models.TextField()
    npwp = models.TextField()
    userid = models.TextField()
    status_transfer = models.BigIntegerField()
    status_kerja = models.ForeignKey(df_status_kerja, on_delete= models.CASCADE)
    status_pegawai = models.ForeignKey(df_status_pegawai, on_delete= models.CASCADE)
    status_nikah = models.ForeignKey(df_status_nikah, on_delete= models.CASCADE)
    agama = models.ForeignKey(df_agama, on_delete= models.CASCADE)
    masih_hidup = models.TextField()
    sudah_berhenti = models.TextField(null=True)
    usia = models.BigIntegerField(null=True)
    masa_kerja = models.TextField()
    kategori_durasi = models.ForeignKey(df_kategori_durasi, on_delete= models.CASCADE)

class df_mutasi(models.Model):
    mutasi_id = models.BigAutoField(primary_key=True)
    nippos = models.ForeignKey(df_sdm, on_delete= models.CASCADE, null=True, blank=True)
    noskep = models.TextField()
    tgl_skep = models.TextField()
    tmt = models.TextField()
    tj = models.TextField()
    jenis_mutasi = models.TextField()
    tgl_brgkt = models.TextField()
    tgl_aktif = models.TextField()
    status = models.TextField()
    userid = models.TextField()
    tgl_insert = models.TextField()
    keterangan = models.TextField()
    level_jabatan = models.TextField()
    uid_insert = models.TextField()
    wkt_update = models.TextField()
    uid_update = models.TextField()
    rumpun = models.TextField()
    tgl_sk = models.TextField()
    nomor_sk = models.TextField()
    tmt_sk = models.TextField()
    rank = models.TextField()
    nopend_asal = models.ForeignKey(df_kantor, on_delete= models.CASCADE, related_name='df_mutasi_asal', null=True, blank=True)
    nopend_tujuan = models.ForeignKey(df_kantor, on_delete= models.CASCADE, related_name='df_mutasi_tujuan', null=True, blank=True)
    next_tmt = models.TextField()
    rank_jabatan = models.TextField()
    durasi_jabatan_sebelumnya = models.TextField()
    masakerja_jabatan_sebelumnya = models.TextField()
    rank_bagian = models.TextField()
    durasi_bagian_sebelumnya = models.TextField()
    masakerja_bagian_sebelumnya = models.TextField()
    rank_jabatan_unitkerja = models.TextField()
    durasi_jabatan_unitkerja_sebelumnya = models.TextField()
    masakerja_jabatan_unitkerja_sebelumnya = models.TextField()
    rank_bagian_unitkerja = models.TextField()
    durasi_bagian_unitkerja_sebelumnya = models.TextField()
    masakerja_bagian_unitkerja_sebelumnya = models.TextField()
    tmt_jabatan = models.TextField()
    tmt_bagian = models.TextField()
    tmt_jabatan_unitkerja = models.TextField()
    tmt_bagian_unitkerja = models.TextField()
    durasi_jabatan = models.TextField()
    masakerja_jabatan = models.TextField()
    durasi_bagian = models.TextField()
    masakerja_bagian = models.TextField()
    durasi_jabatan_unitkerja = models.TextField()
    masakerja_jabatan_unitkerja = models.TextField()
    durasi_bagian_unitkerja = models.TextField()
    masakerja_bagian_unitkerja = models.TextField()
    posisi = models.ForeignKey(df_posisi, on_delete= models.CASCADE, null=True, blank=True)
    bagian = models.ForeignKey(df_bagian, on_delete= models.CASCADE, null=True, blank=True)
    jabatan = models.ForeignKey(df_jabatan, on_delete= models.CASCADE, null=True, blank=True)
    kategori_durasi_jabatan_sebelumnya = models.ForeignKey(df_kategori_durasi, on_delete= models.CASCADE, related_name='df_mutasi_durasi_jabatan_sebelumnya', null=True, blank=True)
    kategori_durasi_bagian_sebelumnya = models.ForeignKey(df_kategori_durasi, on_delete= models.CASCADE, related_name='df_mutasi_durasi_bagian_sebelumnya', null=True, blank=True)
    kategori_durasi_jabatan_unitkerja_sebelumnya = models.ForeignKey(df_kategori_durasi, on_delete= models.CASCADE, related_name='df_mutasi_durasi_jabatan_unitkerja_sebelumnya', null=True, blank=True)
    kategori_durasi_bagian_unitkerja_sebelumnya = models.ForeignKey(df_kategori_durasi, on_delete= models.CASCADE, related_name='df_mutasi_durasi_bagian_unitkerja_sebelumnya', null=True, blank=True)
    kategori_durasi_jabatan = models.ForeignKey(df_kategori_durasi, on_delete= models.CASCADE, related_name='df_mutasi_durasi_jabatan', null=True, blank=True)
    kategori_durasi_bagian = models.ForeignKey(df_kategori_durasi, on_delete= models.CASCADE, related_name='df_mutasi_durasi_bagian', null=True, blank=True)
    kategori_durasi_jabatan_unitkerja = models.ForeignKey(df_kategori_durasi, on_delete= models.CASCADE, related_name='df_mutasi_durasi_jabatan_unitkerja', null=True, blank=True)
    kategori_durasi_bagian_unitkerja = models.ForeignKey(df_kategori_durasi, on_delete= models.CASCADE, related_name='df_mutasi_durasi_bagian_unitkerja', null=True, blank=True)