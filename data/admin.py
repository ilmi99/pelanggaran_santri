from django.contrib import admin

# Register your models here.
from .models import Model_pengurus, Model_santri2, Model_pelanggaran2, Model_kamar, Model_pendidikan

admin.site.register(Model_pengurus)
admin.site.register(Model_santri2)
admin.site.register(Model_pelanggaran2)
admin.site.register(Model_pendidikan)
admin.site.register(Model_kamar)
# admin.site.register(Model_guru)