

from django.db.models import fields
from django.forms import widgets
from tatausaha.models import *

from typing import ClassVar, Tuple
from django.db import models
from django.db.models.deletion import CASCADE, RESTRICT
from django.db.models.fields import AutoField, CharField
from django.db.models.fields.related import ForeignKey
from django.db.models.query import NamedValuesListIterable
from django import forms



# Create your models here.
# relasi guru dan gaji lebih mudah jika menggunakan golongan sebagai fk

class Guru(models.Model):
    nip = models.CharField(max_length=10,primary_key=True,null=False,default=None)
    Nama_Guru = models.CharField(max_length=50,null=False )
    Kelas = models.ForeignKey("tatausaha.Kelas",on_delete=models.RESTRICT)
    Gaji = models.ForeignKey("tatausaha.Gaji", on_delete=models.RESTRICT)
    No_Hp = models.CharField(max_length=12,null=True)
    Alamat = models.CharField(max_length=100,null=True)    
    def __str__(self) :
        return "{}".format(self.Nama_Guru)

class Absensi(models.Model):
    id_absen= models.AutoField(primary_key=True)
    tanggal = models.DateField( auto_now=False, auto_now_add=False)
    kelas = models.ForeignKey("tatausaha.Kelas", on_delete=models.RESTRICT)
    kehadiran = models.CharField(max_length=2)
    keterangan = models.CharField(max_length=50,null=True)
    Mapel = models.ForeignKey("tatausaha.Mapel", on_delete=models.RESTRICT,null=True)
    def __str__(self):
        return "{},{}".format(self.kelas,self.tanggal)


# Model Input

class InputAbsensi(forms.ModelForm):
    class Meta:
        model= Absensi
        fields = [
            'id_absen',
            'tanggal',
            'kelas',
            'kehadiran',
            'keterangan',
            'Mapel'
        ]
        widgets = {
            'tanggal' : forms.DateInput(
                attrs={
                    'class':'form-control',
                    'id':"validationCustom01",
                    'placeholder':"Masukan Tanggal",
                    # "type":"datetime-local"
                    'id':'datetimepicker4',
                    # "data-date-format":"yyyy/mm/dd"
                    
                }
            ),
            'kelas' : forms.Select(
                attrs={
                    'class':'form-control',
                    'id':"validationCustom04",
                    
                }
            ),
            'kehadiran' : forms.TextInput(
                attrs={
                    'class':'form-control',
                    'id':"validationCustom02",
                    'placeholder':"Kehadiran"
                }
            ),
            'keterangan' : forms.TextInput(
                attrs={
                    'class':'form-control',
                    'id':"validationCustom03",
                    'placeholder':"keterangan"
                }
            ),
            'Mapel' : forms.Select(
                attrs={
                    'class':'form-control',
                    'id':"validationCustom05",
                    
                }
            ),
            
        }

