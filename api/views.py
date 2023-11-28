from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
import MySQLdb
import pymysql
pymysql.install_as_MySQLdb()
from .serializers import *

@api_view(['GET'])
def getDataRegional(request):
    regional = df_regional.objects.all()
    serializers = RegionalSerializers(regional, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def getDataAgama(request):
    agama = df_agama.objects.all()
    serializers = AgamaSerializers(agama, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def getDataPosisi(request):
    posisi = df_posisi.objects.all()
    serializers = PosisiSerializers(posisi, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def getDataStatusKerja(request):
    status_kerja = df_status_kerja.objects.all()
    serializers = StatusKerjaSerializers(status_kerja, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def getDataBagian(request):
    bagian = df_bagian.objects.all()
    serializers = BagianSerializers(bagian, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def getDataJabatan(request):
    jabatan = df_jabatan.objects.all()
    serializers = JabatanSerializers(jabatan, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def getDataKantor(request):
    kantor = df_kantor.objects.all()
    serializers = KantorSerializers(kantor, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def getDataSdm(request):
    nippos_param = request.query_params.get('nippos_id', None)
    nama_param = request.query_params.get('nama', None)

    if nippos_param:
        # Jika nippos_param diberikan, filter data berdasarkan nippos
        sdm = df_sdm.objects.filter(nippos=nippos_param)
    elif nama_param:
        sdm = df_sdm.objects.filter(nama=nama_param)
    else:
        # Jika nippos_param tidak diberikan, ambil semua data
        sdm = df_sdm.objects.all()

    # Serialkan data
    serializers = SdmSerializers(sdm, many=True)
    return Response(serializers.data)