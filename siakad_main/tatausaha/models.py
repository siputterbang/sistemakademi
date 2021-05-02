from django.db import models
from django.db.models.deletion import CASCADE, RestrictedError
from django.db.models.enums import Choices
from django.db.models.fields import CharField
from guru.models import *
from murid.models import *
from django.db import IntegrityError
from django import forms


HARI = (('Senin','Senin'),
        ('Selasa','Selasa'),
        ('Rabu','Rabu'),
        ('Kamis','Kamis'),
        ('Jumat','Jumat'),
        ('Sabtu','Sabtu'),
        ('Minggu','Minggu'))
# Create your models here.
class Gaji(models.Model):
    Golongan = models.CharField(max_length=5,null=False,primary_key=True)
    Nominal = models.DecimalField(max_digits=8,decimal_places=0)
    def __str__(self) :
        return "{},{}".format(self.Golongan,self.Nominal)


# class DaftarPelajaran dan nilai
class Kelas(models.Model):
    id_kelas = models.CharField(max_length=5,primary_key=True,null=False)
    nama_kelas =models.CharField(max_length=5)
    def __str__(self):
        return "{},{}".format(self.id_kelas,self.nama_kelas)
    
class Mapel(models.Model):
    id_mapel = models.CharField(null=False,primary_key=True, max_length=10)
    Nama_Pelajaran = models.CharField(null=False, max_length=50)
    
    def __str__(self):
        return "{},{}".format(self.id_mapel,self.Nama_Pelajaran)
    
class Nilai(models.Model):
    id_mapel = models.ForeignKey("Mapel", on_delete=models.RESTRICT)
    nis = models.ForeignKey("murid.Murid", on_delete=models.RESTRICT)
    nilai = models.CharField(max_length=50,null=True)
    keterangan = models.CharField(null=False, max_length=50,default="")
    def __str__(self):
        return "{},{}".format(self.id_mapel,self.nis)

class JadwalPelajaran(models.Model):
    id_kelas = models.ForeignKey("Kelas", on_delete=models.RESTRICT)
    id_mapel = models.ForeignKey("Mapel",on_delete=models.RESTRICT)
    jam_pelajaran = models.CharField(max_length=50,null=True)
    hari = models.CharField(max_length=7,choices=HARI,default='Senin')
    Jumlah_Pertemuan = models.CharField(null=False,max_length=3,default='0')
    def __str__(self):
        return "{}".format(self.id_mapel)
    
# class TampilJadwalPelajaran(models.Model):
#     Kelas = models.CharField(max_length=5)
#     Mapel = models.CharField( max_length=50)
    
#     def __str__(self):
#         return self.Kelas


class InputNilai(forms.ModelForm):
    class Meta:
        model= Nilai
        fields=[
            'id_mapel',
            'nis',
            'nilai',
            'keterangan'
        ]
        widgets = {

            'id_mapel' : forms.Select(
                attrs={
                    'class':'form-control',
                    'id':"validationCustom04",
                    
                }
            ),
            'nis' : forms.Select(
                attrs={
                    'class':'form-control',
                    'id':"validationCustom05",
                    
                }
            ),
            'nilai' : forms.TextInput(
                attrs={
                    'class':'form-control',
                    'id':"validationCustom02",
                    'placeholder':"Nilai"
                }
            ),
            'keterangan' : forms.TextInput(
                attrs={
                    'class':'form-control',
                    'id':"validationCustom03",
                    'placeholder':"Keterangan"
                }
            ),
        }