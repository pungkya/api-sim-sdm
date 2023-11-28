from django.urls import path
from . import views

urlpatterns = [
    path('regional/', views.getDataRegional),
    path('agama/', views.getDataAgama),
    path('posisi/', views.getDataPosisi),
    path('status-kerja/', views.getDataStatusKerja),
    path('bagian/', views.getDataBagian),
    path('jabatan/', views.getDataJabatan),
    path('kantor/', views.getDataKantor),
    path('sdm/', views.getDataSdm),
]