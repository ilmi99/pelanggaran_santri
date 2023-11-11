from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.

class Model_pengurus(models.Model):
	nama_pengurus	= models.CharField(max_length = 30)
	staff	=models.CharField(max_length = 10)
	no_telpon	=models.CharField(max_length = 13)
	username	=models.CharField(max_length = 15)
	email 	=models.CharField(max_length = 15)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_pengurus)
	class Meta:
            verbose_name_plural = "Model_pengurus"

# class Model_guru(models.Model):
# 	nip	= models.CharField(max_length = 30,blank=True, null=True)
# 	nama_guru= models.CharField(max_length = 30,blank=True, null=True)
# 	staff=models.CharField(max_length = 30,blank=True, null=True)
# 	tempat_lahir	=models.CharField(max_length = 35,blank=True, null=True)
# 	tgl_lahir	=models.CharField(max_length = 35,blank=True, null=True)
# 	alamat=models.CharField(max_length = 30,blank=True, null=True)
# 	bidang_studi_yang_diampu =models.CharField(max_length = 30,blank=True, null=True)
# 	nomer_hp=models.CharField(max_length = 15,blank=True, null=True)

# 	published = models.DateTimeField(auto_now_add = True)
# 	updated = models.DateTimeField(auto_now = True)
			
# 	def __str__(self):
# 		return "{}.{}".format(self.id,self.nama_guru)
# 	class Meta:
#             verbose_name_plural = "Model_guru"

class Model_santri2(models.Model):
	id_santri	= models.CharField(max_length = 8,blank=True, null=True)
	nama_santri	= models.CharField(max_length = 30,blank=True, null=True)
	nama_kamar	= models.CharField(max_length = 30,blank=True, null=True)
	tempat_lahir	=models.CharField(max_length = 35,blank=True, null=True)
	tgl_lahir	=models.CharField(max_length = 35,blank=True, null=True)
	alamat	=models.CharField(max_length = 50,blank=True, null=True)
	pendidikan	=models.CharField(max_length = 1500,blank=True, null=True)
	nama_wali	=models.CharField(max_length = 30,blank=True, null=True)
	nomer_hp	=models.CharField(max_length = 13,blank=True, null=True)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_santri)
	class Meta:
            verbose_name_plural = "Model_santri"

class Model_pelanggaran2(models.Model):
	id_pelanggaran	= models.CharField(max_length = 10)
	nama_santri	=models.CharField(max_length = 30)
	nama_kamar	=models.CharField(max_length = 30)
	kategori	=models.CharField(max_length = 6)
	tgl_kejadian	=models.CharField(max_length = 10)
	keterangan	=models.CharField(max_length = 60)
	hukuman	=models.CharField(max_length = 50)
	nama_pengurus	=models.CharField(max_length = 30)
	nomer_hp	=models.CharField(max_length = 13)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.kategori)
	class Meta:
            verbose_name_plural = "Model_pelanggaran"

# kamar
class Model_kamar(models.Model):
	kode_kamar	= models.CharField(max_length = 30)
	nama_kamar	=models.CharField(max_length = 10)
	kapasitas	=models.CharField(max_length = 13)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_kamar)
	class Meta:
            verbose_name_plural = "Model_kamar"
	

# pendidikan
class Model_pendidikan(models.Model):
	kode_pendidikan	= models.CharField(max_length = 30)
	nama_pendidikan	=models.CharField(max_length = 10)
	kelas	=models.CharField(max_length = 13)
	npsn	= models.CharField(max_length = 30,blank=True, null=True)
	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_pendidikan)
	class Meta:
            verbose_name_plural = "Model_pendidikan"