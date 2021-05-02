
from typing import no_type_check
from django.db import models
from django.db.models.deletion import CASCADE
from tatausaha.models import *

# Create your models here.
class Murid(models.Model):
    Nis = models.CharField(max_length=11,primary_key=True,null=False)
    Nama= models.CharField(max_length=50,null=False)
    # Jam_Pelajaran = models.CharField(max_length=11,blank=True)
    Kelas = models.ForeignKey("tatausaha.Kelas",on_delete=models.RESTRICT)
    Alamat=models.CharField(max_length=50,null=True)
    No_Hp= models.CharField(max_length=13,null=True)
    # Mata_Pelajaran = models.ForeignKey('tatausaha.MataPelajaran', on_delete=models.CASCADE,null=True)
    def __str__(self) :
        return "{},{}".format(self.Nama,self.Kelas)
