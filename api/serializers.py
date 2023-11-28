from rest_framework import serializers

from .models import *

class RegionalSerializers(serializers.ModelSerializer):
    class Meta:
        model = df_regional
        fields = '__all__'

class AgamaSerializers(serializers.ModelSerializer):
    class Meta:
        model = df_agama
        fields = '__all__'

class PosisiSerializers(serializers.ModelSerializer):
    class Meta:
        model = df_posisi
        fields = '__all__'

class StatusPegawaiSerializers(serializers.ModelSerializer):
    class Meta:
        model = df_status_pegawai
        fields = '__all__'

class StatusKerjaSerializers(serializers.ModelSerializer):
    class Meta:
        model = df_status_kerja
        fields = '__all__'

class BagianSerializers(serializers.ModelSerializer):
    class Meta:
        model = df_bagian
        fields = '__all__'

class JabatanSerializers(serializers.ModelSerializer):
    class Meta:
        model = df_jabatan
        fields = '__all__'

class KantorSerializers(serializers.ModelSerializer):
    class Meta:
        model = df_kantor
        fields = '__all__'

class SdmSerializers(serializers.ModelSerializer):
    class Meta:
        model = df_sdm
        fields = '__all__'