from django.shortcuts import render
from django.http import HttpResponse

from tatausaha.models import JadwalPelajaran as Jadwal
from tatausaha.models import Nilai
from django.contrib.auth.models import Group,User
from murid.models import Murid 
from django.contrib.auth.decorators import user_passes_test
import time
bulan = ("Januari", "Pebruari", "Maret","April", "Mei", "Juni",
        "Juli", "Agustus", "September", "Oktober", "Nopember", "Desember")
day = ("Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu")
sekarang = time.time()
infowaktu = time.localtime(sekarang)
# print( "Tanggal", infowaktu[2], bulan[infowaktu[1]-1], infowaktu[0])
# print( "Hari", hari[infowaktu[6]])
today  = day[infowaktu[6]]
# Create your views here.
def cekuser(user):
    grub = Group.objects.get(name='Murid')
    usrgrub = user.groups.all()
    stts = grub in usrgrub
    return stts



# murid bisa lihat jadwal& mapel. Bisa lihat nilai dirinya. bisa melihat kelasnya.
# layout
# jadwal    sudah          \ tugas (comingsoon)  
# mapel yang diikuti sudah
# seluruh jadwalsudah

def namakelas(request):
    kelasmurid = User.objects.filter(username__startswith=str(request.user)).values()
    nis = [i['first_name'] for i in kelasmurid]
    getKelas = Murid.objects.filter(Nis=nis[0]).values()
    kelasmurid = [i['Kelas_id'] for i in getKelas]
    return str(kelasmurid[0][3:])

def namauser(request):
    kelasmurid = User.objects.filter(username__startswith=str(request.user)).values()
    nis = [i['first_name'] for i in kelasmurid]
    getKelas = Murid.objects.filter(Nis=nis[0]).values()
    kelasmurid = [i['Nama'] for i in getKelas]
    return str(kelasmurid[0])
    
@user_passes_test(cekuser)
def dashboardmurid(request):
    # nilai = Nilai.objects.filter(nis__Nama='Fadli')
    print()
    # wkek berhasil .          
    # print(Nilai.objects.filter(nis__Nama='Alfian'),'huhuhuhuh') 
    # print(nilai,'hihihihi')
    # print(Nilai.objects.order_by('nis'),"HUHUHUHUHUH")
    # if Nilai.objects.filter(nis="Alfian,1907D,7D"):
    #     print("There is at least one Entry with the headline Test")
    jadwal =  Jadwal.objects.filter(id_kelas__nama_kelas=namakelas(request))
    context={
        'hari':today,
        'jadwalmapel' : jadwal,
        'jadwalhariini': jadwal.filter(hari=str(today)),
        'namauser': namauser(request)
        # 'nilaisiswa' : nilai
    }
    print(jadwal)
    return render(request,'murid.html',context)