# data santri
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path(r'^Santri/$',Data_Santri, name="Santri"),
    path(r'^Tambah_Santri/$',Tambah_Santri, name="Tambah_Santri"),
    path(r'^hapus_Santri/(?P<hapus_s>[0-9]+)$',Hapus_Santri, name="hapus_Santri"),
    path(r'^edit_Santri/(?P<id_s>[0-9]+)$',Edit_Santri, name="edit_Santri"),
    # data pelanggaran

	#pengurus
	path(r'^Pengurus/$',Data_Pengurus, name="Pengurus"),
    path(r'^Tambah_Pengurus/$',Tambah_Pengurus, name="Tambah_Pengurus"),
    path(r'^hapus_Pengurus/(?P<hapus_pg>[0-9]+)$',Hapus_Pengurus, name="hapus_Pengurus"),
    path(r'^edit_Pengurus/(?P<id_pg>[0-9]+)$',Edit_Pengurus, name="edit_Pengurus"),
    
]

    # url(r'^Santri/$',Data_Santri, name="Santri"),
    # url(r'^Tambah_Santri/$',Tambah_Santri, name="Tambah_Santri"),
    # url(r'^hapus_Santri/(?P<hapus_s>[0-9]+)$',Hapus_Santri, name="hapus_Santri"),
    # url(r'^edit_Santri/(?P<id_s>[0-9]+)$',Edit_Santri, name="edit_Santri"),
    # # data pelanggaran
    
#     # pengurus
#     url(r'^Pengurus/$',Data_Pengurus, name="Pengurus"),
#     url(r'^Tambah_Pengurus/$',Tambah_Pengurus, name="Tambah_Pengurus"),
#     url(r'^hapus_Pengurus/(?P<hapus_pg>[0-9]+)$',Hapus_Pengurus, name="hapus_Pengurus"),
#     url(r'^edit_Pengurus/(?P<id_pg>[0-9]+)$',Edit_Pengurus, name="edit_Pengurus"),
urlpatterns += staticfiles_urlpatterns()




# pengurus


# data santri
def Data_Santri(request):
	tampil_santri = Model_santri.objects.all()
	context = {	
	'tampil_santri': tampil_santri,
	}
	return render(request, 'Master_data/data_santri/tabel.html',  context)	

def Tambah_Santri(request):
	if request.method == 'POST':
		Model_santri.objects.create(
			id_santri = request.POST['id_santri'],
			nama_santri = request.POST['nama_santri'],
			tempat_tgl_lahir = request.POST['tempat_tgl_lahir'],			
			alamat = request.POST['alamat'],			
			pendidikan = request.POST['pendidikan'],			
			nama_wali = request.POST['nama_wali'],			
			nomer_hp = request.POST['nomer_hp'],			
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/Santri/")	
	context = {	
	'Tambah': 'Tambah'
	}
	return render(request, 'Master_data/data_santri/tambah.html', context)

def Hapus_Santri(request, hapus_s):
	Model_santri.objects.filter(id=hapus_s).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('Santri')			

def Edit_Santri(request, id_s):		
	edit_santri = Model_santri.objects.get(id=id_s)
	if request.method == 'POST':		
			edit_santri.id_santri = request.POST.get('id_santri')
			edit_santri.nama_santri = request.POST.get('nama_santri')			
			edit_santri.tempat_tgl_lahir = request.POST.get('tempat_tgl_lahir')						
			edit_santri.alamat = request.POST.get('alamat')						
			edit_santri.pendidikan = request.POST.get('pendidikan')						
			edit_santri.nama_wali = request.POST.get('nama_wali')						
			edit_santri.nomer_hp = request.POST.get('nomer_hp')						
			edit_santri.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('Santri')

	context = {'edit_santri': edit_santri}
	return render(request, 'Master_data/data_santri/edit.html',  context)

# pelanggaran
