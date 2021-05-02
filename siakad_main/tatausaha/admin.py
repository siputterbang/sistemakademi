#from siakad_main.tatausaha.models import Gaji
from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Gaji)
admin.site.register(Kelas)
admin.site.register(Mapel)
admin.site.register(Nilai)
admin.site.register(JadwalPelajaran)

