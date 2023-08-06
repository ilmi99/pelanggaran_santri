from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from .decorators import tolakhalaman_ini, ijinkan_pengguna, pilihan_login
from django.contrib.auth.decorators import login_required

from .models import Model_alumni, Model_guru, Model_pengurus, Model_santri2, Model_pelanggaran2, Model_kamar, Model_pendidikan
import hashlib

@tolakhalaman_ini
def index(request):
	context = {
	'page_title':'Login',
	}
	print(request.user)
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('Home')
		

	return render(request, 'index.html',  context)

# @login_required(login_url='login')
# @pilihan_login
def HomeView(request):	
	jumlah = Model_pelanggaran2.objects.count()
	context = {
	'page_title':'Home',
	'jumlah':jumlah
	}
	test_group = Group.objects.get(name="pengurus")
	admin_group = request.user.groups.all()

	template_name = None
	if test_group in admin_group:
		template_name = 'halaman_pengurus.html'
	else:
		template_name = 'home.html'

	return render(request, template_name,  context)
	# return render(request, 'home.html',  context)

def LogoutView(request):
	context = {
	'page_title':'logout',
	}
	# if request.method == "POST":
	# 	if request.POST["logout"] == "Submit":	
	logout(request)

	return redirect('index')

	# return render(request, 'logout.html',  context)	

@ijinkan_pengguna(yang_diizinkan=['admin'])
@login_required(login_url='login')
def Data_Santri(request):
	tampil_santri = Model_santri2.objects.all()
	context = {	
	'tampil_santri': tampil_santri,
	}
	return render(request, 'Master_data/data_santri/tabel.html',  context)	

@ijinkan_pengguna(yang_diizinkan=['admin'])
@login_required(login_url='login')
def Tambah_Santri(request):
	kode = Model_santri2.objects.count()
	kode_otomatis = kode +1
	select_pendidikan = Model_pendidikan.objects.all()	
	select_kamar = Model_kamar.objects.all()
	if request.method == 'POST':
		Model_santri2.objects.create(
			id_santri = request.POST['id_santri'],
			nama_santri = request.POST['nama_santri'],
			nama_kamar = request.POST['nama_kamar'],
			tempat_tgl_lahir = request.POST['tempat_tgl_lahir'],			
			alamat = request.POST['alamat'],			
			pendidikan = request.POST['pendidikan'],			
			nama_wali = request.POST['nama_wali'],
			nomer_hp = request.POST['nomer_hp'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/Santri/")	
	context = {	
	'Tambah': 'Tambah',
	'select_kamar': select_kamar,
	'select_pendidikan': select_pendidikan,
	'kode_otomatis':kode_otomatis
	}
	return render(request, 'Master_data/data_santri/tambah.html', context)

@ijinkan_pengguna(yang_diizinkan=['admin'])
@login_required(login_url='login')
def Hapus_Santri(request, hapus_s):
	Model_santri2.objects.filter(id=hapus_s).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('Santri')			

@ijinkan_pengguna(yang_diizinkan=['admin'])
@login_required(login_url='login')
def Edit_Santri(request, id_s):	
	select_pendidikan = Model_pendidikan.objects.all()	
	select_kamar = Model_kamar.objects.all()	
	edit_santri = Model_santri2.objects.get(id=id_s)
	if request.method == 'POST':		
			edit_santri.id_santri = request.POST.get('id_santri')
			edit_santri.nama_santri = request.POST.get('nama_santri')			
			edit_santri.nama_kamar = request.POST.get('nama_kamar')	
			edit_santri.tempat_tgl_lahir = request.POST.get('tempat_tgl_lahir')						
			edit_santri.alamat = request.POST.get('alamat')						
			edit_santri.pendidikan = request.POST.get('pendidikan')						
			edit_santri.nama_wali = request.POST.get('nama_wali')
			edit_santri.nomer_hp = request.POST.get('nomer_hp')
			edit_santri.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('Santri')

	context = {
	'edit_santri': edit_santri, 
	'select_kamar': select_kamar,
	'select_pendidikan': select_pendidikan
	}
	return render(request, 'Master_data/data_santri/edit.html',  context)

# pelanggaran
@ijinkan_pengguna(yang_diizinkan=['admin'])
@login_required(login_url='login')
def Data_Pelanggaran(request):
	data_pelanggaran = Model_pelanggaran2.objects.all()
	context = {	
	'data_pelanggaran': data_pelanggaran,
	}
	return render(request, 'Master_data/data_pelanggaran/tabel.html',  context)	

# proses pelanggaran santri
@ijinkan_pengguna(yang_diizinkan=['admin'])
@login_required(login_url='login')
def list_santri(request):
	tampil_santri = Model_santri2.objects.all()
	context = {	
	'tampil_santri': tampil_santri,
	}
	return render(request, 'Master_data/data_pelanggaran/proses_pelanggaran.html',  context)	

@ijinkan_pengguna(yang_diizinkan=['admin'])
@login_required(login_url='login')
def Tambah_Pelanggaran(request, id_sp):
	kode = Model_santri2.objects.count()
	kode_otomatis = kode + 1

	proses_santri = Model_santri2.objects.get(id=id_sp)
	if request.method == 'POST':
		Model_pelanggaran2.objects.create(
			id_pelanggaran = request.POST['id_pelanggaran'],
			nama_santri = request.POST['nama_santri'],
			nama_kamar = request.POST['nama_kamar'],
			kategori = request.POST['kategori'],			
			tgl_kejadian = request.POST['tgl_kejadian'],			
			keterangan = request.POST['keterangan'],			
			hukuman = request.POST['hukuman'],			
			nama_pengurus = request.POST['nama_pengurus'],
			nomer_hp = request.POST['nomer_hp'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/Pelanggaran/")	
	context = {	
	'Tambah': 'Tambah',
	'proses_santri': proses_santri,
	'kode_otomatis': kode_otomatis
	}
	return render(request, 'Master_data/data_pelanggaran/tambah.html', context)

@ijinkan_pengguna(yang_diizinkan=['admin'])
@login_required(login_url='login')
def Hapus_Pelanggaran(request, hapus_p):
	Model_pelanggaran2.objects.filter(id=hapus_p).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('Pelanggaran')			

@ijinkan_pengguna(yang_diizinkan=['admin'])
@login_required(login_url='login')
def Edit_Pelanggaran(request, id_p):		
	edit_pelanggaran = Model_pelanggaran2.objects.get(id=id_p)
	if request.method == 'POST':		
			edit_pelanggaran.id_pelanggaran = request.POST.get('id_pelanggaran')
			edit_pelanggaran.nama_santri = request.POST.get('nama_santri')
			edit_pelanggaran.nama_kamar = request.POST.get('nama_kamar')
			edit_pelanggaran.kategori = request.POST.get('kategori')						
			edit_pelanggaran.tgl_kejadian = request.POST.get('tgl_kejadian')						
			edit_pelanggaran.keterangan = request.POST.get('keterangan')						
			edit_pelanggaran.hukuman = request.POST.get('hukuman')						
			edit_pelanggaran.nama_pengurus = request.POST.get('nama_pengurus')
			edit_pelanggaran.nomer_hp = request.POST.get('nomer_hp')
			edit_pelanggaran.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('Pelanggaran')

	context = {'edit_pelanggaran': edit_pelanggaran}
	return render(request, 'Master_data/data_pelanggaran/edit.html',  context)

# #pengurus
@ijinkan_pengguna(yang_diizinkan=['admin'])
@login_required(login_url='login')
def Data_Pengurus(request):
	tampil_pengurus = Model_pengurus.objects.all()
	context = {	
	'tampil_pengurus': tampil_pengurus,
	}
	return render(request, 'Master_data/data_pengurus/tabel.html',  context)	

@ijinkan_pengguna(yang_diizinkan=['admin'])
@login_required(login_url='login')
def Tambah_Pengurus(request):
	form = RegisterForm()
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			nilaiuser=form.cleaned_data.get('username')
			group_pengurus=form.save()
			grup=Group.objects.get(name='pengurus')
			group_pengurus.groups.add(grup)
			# return redirect('/')   
			Model_pengurus.objects.create(
				nama_pengurus = request.POST['nama_pengurus'],
				staff = request.POST['staff'],
				no_telpon = request.POST['no_telepon'],			
				username = request.POST['username'],			
				email = request.POST['email'],			
				)
			messages.info(request, 'Data Berhasil Di Simpan..')
			return redirect("/Pengurus/")	
	context = {	
	'form' : form,
	'Tambah siswa': 'Tambah siswa'
	}
	return render(request, 'Master_data/data_pengurus/tambah.html', context)

@ijinkan_pengguna(yang_diizinkan=['admin'])
@login_required(login_url='login')
def Hapus_Pengurus(request, hapus_pg):
	Model_pengurus.objects.filter(id=hapus_pg).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('Pengurus')			

@ijinkan_pengguna(yang_diizinkan=['admin'])
@login_required(login_url='login')
def Edit_Pengurus(request, id_pg):		
	edit_pengurus = Model_pengurus.objects.get(id=id_pg)
	if request.method == 'POST':		
			edit_pengurus.nama_pengurus = request.POST.get('nama_pengurus')
			edit_pengurus.staff = request.POST.get('staff')			
			edit_pengurus.no_telpon = request.POST.get('no_telepon')						
			edit_pengurus.username = request.POST.get('username')						
			edit_pengurus.emailmail = request.POST.get('email')						
			edit_pengurus.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('Pengurus')

	context = {'edit_pengurus': edit_pengurus}
	return render(request, 'Master_data/data_pengurus/edit.html',  context)


# pelanggaran pengurus
# pelanggaran
@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['pengurus'])
def Data_Pelanggaran_pengurus(request):
	data_pelanggaran = Model_pelanggaran2.objects.all()
	context = {	
	'data_pelanggaran': data_pelanggaran,
	}
	return render(request, 'Master_pengurus/data_pelanggaran/tabel.html',  context)	

# proses pelanggaran santri
@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['pengurus'])
def list_santri_pengurus(request):
	tampil_santri = Model_santri2.objects.all()
	context = {	
	'tampil_santri': tampil_santri,
	}
	return render(request, 'Master_pengurus/data_pelanggaran/proses_pelanggaran.html',  context)	

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['pengurus'])
def Tambah_Pelanggaran_pengurus(request, id_spp):
	proses_santri = Model_santri2.objects.get(id=id_spp)
	if request.method == 'POST':
		Model_pelanggaran2.objects.create(
			id_pelanggaran = request.POST['id_pelanggaran'],
			nama_santri = request.POST['nama_santri'],
			nama_kamar = request.POST['nama_kamar'],
			kategori = request.POST['kategori'],			
			tgl_kejadian = request.POST['tgl_kejadian'],			
			keterangan = request.POST['keterangan'],			
			hukuman = request.POST['hukuman'],			
			nama_pengurus = request.POST['nama_pengurus'],
			nomer_hp = request.POST['nomer_hp'],
		    )
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/Pelanggaran_pengurus/")	
	context = {	
	'Tambah': 'Tambah',
	'proses_santri': proses_santri
	}
	return render(request, 'Master_pengurus/data_pelanggaran/tambah.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['pengurus'])
def Hapus_Pelanggaran_pengurus(request, hapus_sp):
	Model_pelanggaran2.objects.filter(id=hapus_sp).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('Pelanggaran_pengurus')			

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['pengurus'])
def Edit_Pelanggaran_pengurus(request, id_pp):		
	edit_pelanggaran = Model_pelanggaran2.objects.get(id=id_pp)
	if request.method == 'POST':		
			edit_pelanggaran.id_pelanggaran = request.POST.get('id_pelanggaran')
			edit_pelanggaran.nama_santri = request.POST.get('nama_santri')
			edit_pelanggaran.nama_kamar = request.POST.get('nama_kamar')
			edit_pelanggaran.kategori = request.POST.get('kategori')						
			edit_pelanggaran.tgl_kejadian = request.POST.get('tgl_kejadian')						
			edit_pelanggaran.keterangan = request.POST.get('keterangan')						
			edit_pelanggaran.hukuman = request.POST.get('hukuman')						
			edit_pelanggaran.nama_pengurus = request.POST.get('nama_pengurus')
			edit_pelanggaran.nomer_hp = request.POST.get('nomer_hp')
			edit_pelanggaran.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('Pelanggaran_pengurus')

	context = {'edit_pelanggaran': edit_pelanggaran}
	return render(request, 'Master_pengurus/data_pelanggaran/edit.html',  context)

# data pelanggaran
@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def Data_kamar(request):
	tampil = Model_kamar.objects.all()
	context = {	
	'tampil': tampil,
	}
	return render(request, 'Master_data/data_kamar/tabel.html',  context)	

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def Tambah_kamar(request):
	kode = Model_kamar.objects.count()
	kode_otomatis = kode + 1
	if request.method == 'POST':
		Model_kamar.objects.create(
			kode_kamar = request.POST['kode_kamar'],
			nama_kamar = request.POST['nama_kamar'],
			kapasitas = request.POST['kapasitas'],			
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/Kamar/")	
	context = {	
	'Tambah': 'Tambah',
	'kode_otomatis': kode_otomatis
	}
	return render(request, 'Master_data/data_kamar/tambah.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def Hapus_kamar(request, hapus_kamar):
	Model_kamar.objects.filter(id=hapus_kamar).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('Kamar')

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def Edit_kamar(request, id_kamar):
	edit_data = Model_kamar.objects.get(id=id_kamar)
	if request.method == 'POST':		
			edit_data.kode_kamar = request.POST.get('kode_kamar')
			edit_data.nama_kamar = request.POST.get('nama_kamar')			
			edit_data.kapasitas = request.POST.get('kapasitas')						
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('Kamar')

	context = {'edit_data': edit_data}
	return render(request, 'Master_data/data_kamar/edit.html',  context)

# pendidikan
@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def Data_pendidikan(request):
	tampil = Model_pendidikan.objects.all()
	context = {	
	'tampil': tampil,
	}
	return render(request, 'Master_data/data_pendidikan/tabel.html',  context)	

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def Tambah_pendidikan(request):
	kode = Model_pendidikan.objects.count()
	kode_otomatis = kode + 1
	if request.method == 'POST':
		Model_pendidikan.objects.create(
			kode_pendidikan = request.POST['kode_pendidikan'],
			nama_pendidikan = request.POST['nama_pendidikan'],
			kelas = request.POST['kelas'],			
			npsn = request.POST['npsn'],			
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/Pendidikan/")	
	context = {	
	'Tambah': 'Tambah',
	'kode_otomatis': kode_otomatis
	}
	return render(request, 'Master_data/data_pendidikan/tambah.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def Hapus_pendidikan(request, hapus_pendidikan):
	Model_pendidikan.objects.filter(id=hapus_pendidikan).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('Pendidikan')

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def Edit_pendidikan(request, id_pendidikan):
	edit_data = Model_pendidikan.objects.get(id=id_pendidikan)
	if request.method == 'POST':		
			edit_data.kode_pendidikan = request.POST.get('kode_pendidikan')
			edit_data.nama_pendidikan = request.POST.get('nama_pendidikan')			
			edit_data.kelas = request.POST.get('kelas')						
			edit_data.npsn = request.POST.get('npsn')						
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('Pendidikan')

	context = {'edit_data': edit_data}
	return render(request, 'Master_data/data_pendidikan/edit.html',  context)

# Guru
@ijinkan_pengguna(yang_diizinkan=['admin'])
@login_required(login_url='login')
def Data_guru(request):
	tampil_guru = Model_guru.objects.all()
	context = {	
	'tampil_guru': tampil_guru,
	}
	return render(request, 'Master_data/data_guru/tabel.html',  context)	

@ijinkan_pengguna(yang_diizinkan=['admin'])
@login_required(login_url='login')
def Tambah_guru(request):
	if request.method == 'POST':
		Model_guru.objects.create(
			nip = request.POST['nip'],
			nama_guru = request.POST['nama_guru'],
			staff = request.POST['staff'],
			tempat_tgl_lahir = request.POST['tempat_tgl_lahir'],			
			alamat = request.POST['alamat'],			
			bidang_studi_yang_diampu = request.POST['bidang_studi_yang_diampu'],			
			# nama_wali = request.POST['nama_wali'],
			nomer_hp = request.POST['nomer_hp'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/Guru/")	
	context = {	
	'Tambah': 'Tambah',
	}
	return render(request, 'Master_data/data_guru/tambah.html', context)
@ijinkan_pengguna(yang_diizinkan=['admin'])
@login_required(login_url='login')
def Hapus_guru(request, hapus_guru):
	Model_guru.objects.filter(id=hapus_guru).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('Guru')			

@ijinkan_pengguna(yang_diizinkan=['admin'])
@login_required(login_url='login')
def Edit_guru(request, id_guru):	
	# select_pendidikan = Model_pendidikan.objects.all()	
	# select_kamar = Model_kamar.objects.all()	
	edit_guru = Model_guru.objects.get(id=id_guru)
	if request.method == 'POST':		
			edit_guru.nip = request.POST.get('nip')
			edit_guru.nama_guru = request.POST.get('nama_guru')			
			edit_guru.staff = request.POST.get('staff')	
			edit_guru.tempat_tgl_lahir = request.POST.get('tempat_tgl_lahir')						
			edit_guru.alamat = request.POST.get('alamat')						
			edit_guru.bidang_studi_yang_diampu = request.POST.get('bidang_studi_yang_diampu')						
			edit_guru.nomer_hp  = request.POST.get('nomer_hp ')
			edit_guru.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('Guru')

	context = {
	'edit_guru': edit_guru, 
	# 'select_kamar': select_kamar,
	# 'select_pendidikan': select_pendidikan
	}
	return render(request, 'Master_data/data_guru/edit.html',  context)

# pelanggaran
@ijinkan_pengguna(yang_diizinkan=['admin'])
@login_required(login_url='login')
def Data_Pelanggaran(request):
	data_pelanggaran = Model_pelanggaran2.objects.all()
	context = {	
	'data_pelanggaran': data_pelanggaran,
	}
	return render(request, 'Master_data/data_pelanggaran/tabel.html',  context)	


# laporan menu

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def Menu_laporan(request):
	context = {	
	'menu':'menu'
	}
	return render(request, 'Master_data/laporan/menu_lp.html',  context)	

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def LP_Pengurus(request):
	LP_Pengurus = Model_pengurus.objects.all()
	context = {	
	'LP_Pengurus': LP_Pengurus,
	}
	return render(request, 'Master_data/laporan/lp_pengurus.html',  context)	

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def LP_pelanggaran(request):
	LP_pelanggaran = Model_pelanggaran2.objects.all()
	context = {	
	'LP_pelanggaran': LP_pelanggaran,
	}
	return render(request, 'Master_data/laporan/lp_pelanggaran.html',  context)	

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def LP_santri(request):
	LP_santri = Model_santri2.objects.all()
	context = {	
	'LP_santri': LP_santri,
	}
	return render(request, 'Master_data/laporan/LP_santri.html',  context)	

def Data_alumni(request):
	tampil_alumni = Model_alumni.objects.all()
	context = {	
	'tampil_alumni': tampil_alumni,
	}
	return render(request, 'Master_data/data_pengurus/tabel.html',  context)	
