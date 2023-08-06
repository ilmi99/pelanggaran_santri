from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    path('Home/', views.HomeView, name='Home'),
    path('logout/', views.LogoutView, name='logout'),

    # # data santri
    path(r'Santri/', views.Data_Santri, name='Santri'),
    path(r'Tambah_Santri/', views.Tambah_Santri, name='Tambah_Santri'),
    path(r'hapus_Santri,?P<hapus_s>[0-9]+)', views.Hapus_Santri, name='hapus_Santri'),
    path(r'edit_Santri,?P<id_s>[0-9]+)',views.Edit_Santri, name='edit_Santri'),

    # # kamar
    path(r'Kamar/', views.Data_kamar, name='Kamar'),
    path(r'Tambah_kamar/', views.Tambah_kamar, name='Tambah_kamar'),
    path(r'hapus_kamar,?P<hapus_kamar>[0-9]+)', views.Hapus_kamar, name='hapus_kamar'),
    path(r'edit_kamar,?P<id_kamar>[0-9]+)', views.Edit_kamar, name='edit_kamar'),

    # # pendidikan
    path(r'Pendidikan/', views.Data_pendidikan, name='Pendidikan'),
    path(r'Tambah_pendidikan/', views.Tambah_pendidikan, name='Tambah_pendidikan'),
    path(r'hapus_pendidikan/?P<hapus_pendidikan>[0-9]+)', views.Hapus_pendidikan, name='hapus_pendidikan'),
    path(r'edit_pendidikan/?P<id_pendidikan>[0-9]+)', views.Edit_pendidikan, name='edit_pendidikan'),
   
    #  Guru   
    path(r'Guru/', views.Data_guru, name='Guru'),
    path(r'Tambah_guru/', views.Tambah_guru, name='Tambah_guru'),
    path(r'hapus_guru/?P<hapus_guru>[0-9]+)', views.Hapus_guru, name='hapus_guru'),
    path(r'edit_guru/?P<id_guru>[0-9]+)', views.Edit_guru, name='edit_guru'),

    # # pelanggaran
    path(r'Pelanggaran/', views.Data_Pelanggaran, name='Pelanggaran'),
    path(r'list_santri/', views.list_santri, name='list_santri'),
    path(r'hapus_Pelanggaran/?P<hapus_p>[0-9]+)', views.Hapus_Pelanggaran, name='hapus_Pelanggaran'),
    path(r'edit_Pelanggaran/?P<id_p>[0-9]+)', views.Edit_Pelanggaran, name='edit_Pelanggaran'),
    path(r'Tambah_Pelanggaran/?P<id_sp>[0-9]+)', views.Tambah_Pelanggaran, name='Tambah_Pelanggaran'),

    # # pengurus
    path(r'Pengurus/', views.Data_Pengurus, name='Pengurus'),
    path(r'Tambah_Pengurus/', views.Tambah_Pengurus, name='Tambah_Pengurus'),
    path(r'hapus_pengurus/?P<hapus_pg>[0-9]+)', views.Hapus_Pengurus, name='hapus_Pengurus'),
    path(r'edit_Pengurus/?P<id_pg>[0-9]+)', views.Edit_Pengurus, name='edit_Pengurus'),
  
    # # # pelanggaran pengurus
    path(r'Pelanggaran_pengurus/', views.Data_Pelanggaran_pengurus, name='Pelanggaran_pengurus'),
    path(r'list_santri_pengurus/', views.list_santri_pengurus, name='list_santri_pengurus'),
    path(r'Tambah_Pelanggaran_pengurus/?P<id_spp>[0-9]+)', views.Tambah_Pelanggaran_pengurus, name='Tambah_Pelanggaran_pengurus'),
    path(r'hapus_Pelanggaran_pengurus/?P<hapus_sp>[0-9]+)', views.Hapus_Pelanggaran_pengurus, name='hapus_Pelanggaran_pengurus'),
    path(r'edit_Pelanggaran_pengurus/?P<id_pp>[0-9]+)', views.Edit_Pelanggaran_pengurus, name='edit_Pelanggaran_pengurus'),

    # # menu laporan
    path(r'Menu_laporan/', views.Menu_laporan, name='Menu_laporan'),

    # # lp pelanggaran
    path(r'LP_Pengurus/', views.LP_Pengurus, name='LP_Pengurus'),
    path(r'LP_pelanggaran/', views.LP_pelanggaran, name='LP_pelanggaran'),
    path(r'LP_santri/', views.LP_santri, name='LP_santri'),

]
urlpatterns += staticfiles_urlpatterns()

