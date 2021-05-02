
from django.forms.forms import Form
from django.shortcuts import redirect, render
from django.http import HttpResponse
from murid.models import Murid 
from tatausaha.models import *
from .models import *
from django.contrib.auth.models import Group,User
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

# cekpoint
def cekuser(user):
    grub = Group.objects.get(name='GuruMapel')
    usrgrub = user.groups.all()
    stts = grub in usrgrub
    return stts

def namakelas(request):
    walikelas = User.objects.filter(username__startswith=str(request.user)).values()
    nip = [i['first_name'] for i in walikelas]
    getKelas = Guru.objects.filter(nip=nip[0]).values()
    kelasguru = [i['Kelas_id'] for i in getKelas]
    return str(kelasguru[0][3:])

def namauser(request):
    walikelas = User.objects.filter(username__startswith=str(request.user)).values()
    nip = [i['first_name'] for i in walikelas]
    getKelas = Guru.objects.filter(nip=nip[0]).values()
    kelasguru = [i['Nama_Guru'] for i in getKelas]
    return str(kelasguru[0])
# Create your views here.
@user_passes_test(cekuser)
def dashboardguru(request):
    # walikelas = User.objects.filter(username__startswith=str(request.user)).values()
    # nip = [i['first_name'] for i in walikelas]
    # getKelas = Guru.objects.filter(nip=nip[0]).values()
    # kelasguru = [i['Kelas_id'] for i in getKelas]
    # get(username=str(request.user))
    # kelas_diampu =  Guru.objects.get( Nama_Guru=str(Supardi))
    murids = Murid.objects.filter(Kelas__nama_kelas=namakelas(request))
    jadwal = JadwalPelajaran.objects.filter(id_kelas__nama_kelas=namakelas(request))
    kehadiran = Absensi.objects.filter(kelas__nama_kelas=namakelas(request))
    # mapel = Mapel.objects.filter()
    # print(jadwal.filter(hari=str(today)),'debug',today)
    # print(jadwal.filter(id_mapel__id_mapel='PKN1907'))
    # print(str(walikelas),'jelas diampu')
    # for i in walikelas:
    #     print(i['first_name'])
    print(namauser(request),'huhuhuhuh')

    if request.user.is_authenticated:
        usrauthstts = 'True'
    else:
        usrauthstts = 'False'
        return redirect('dashboardguru:forbidden')

    context={
        'namauser':namauser(request),
        'murids':murids,
        'jadwalmapel' : jadwal,
        'absensi':kehadiran,
        'jmlmapel': jadwal.count(),
        'jmlsiswa': murids.count(),
        'hari' : today,
        'jadwalhariini': jadwal.filter(hari=str(today)),
        'auth':usrauthstts
        
    }
    return render(request,'Dashboard.html',context)
@user_passes_test(cekuser)
def dasboardcart(request):
    context={
        'namauser':namauser(request),
    }
    return render(request,'charts.html',context)

@user_passes_test(cekuser)
def dasboardtables(request):
    murids = Murid.objects.filter(Kelas__nama_kelas=namakelas(request))
    context={
        'murid': murids,
        'namauser':namauser(request),
    }
    return render(request,'tables.html',context)

@user_passes_test(cekuser)
def absensi(request):
    FormAbsensi = InputAbsensi(request.POST or None)
    if request.method == 'POST':
        if FormAbsensi.is_valid():
            FormAbsensi.save()
            return redirect('dashboardguru:tampilabsen')


    context={
        'absen' : FormAbsensi,
        'namauser':namauser(request),
    }
    return render(request,'absensi.html',context)

@user_passes_test(cekuser)
def tampilabsen(request):
    kehadiran = Absensi.objects.filter(kelas__nama_kelas=namakelas(request))
    print(kehadiran)
    for i in kehadiran:
        print(i.id_absen,i.tanggal,i.kelas,i.Mapel)
    context={
        'tampilabsen':kehadiran,
        'namauser':namauser(request),
    }
    return render(request,'tampilabsen.html',context)

@user_passes_test(cekuser)
def jadwal(request):
    jadwal = JadwalPelajaran.objects.filter(id_kelas__nama_kelas=namakelas(request))
    context={
        'jadwalmapel' : jadwal,
        'namauser':namauser(request),
    }
    return render(request,'jadwal.html',context)
@user_passes_test(cekuser)
def forbidden(req):
    return render(req,'404.html')
@user_passes_test(cekuser)
def inputnilai(request):
    FormNilai = InputNilai(request.POST or None)
    if request.method == 'POST':
        if FormNilai.is_valid():
            FormNilai.save()
            return redirect('dashboardguru:tampilabsen')
    context={
        'inputnilai' : FormNilai,
        'namauser':namauser(request),
    }
    return render(request,'inputnilai.html',context)

@user_passes_test(cekuser)
def hapusabsen(request,delid):
    Absensi.objects.filter( id_absen=delid).delete()
    return redirect('dashboardguru:tampilabsen')
@user_passes_test(cekuser)
def editabsen(request,editid):
    update_absen= Absensi.objects.get(id_absen=editid)
    data = {
            'id_absen':update_absen.id_absen,
            'tanggal':update_absen.tanggal,
            'kelas':update_absen.kelas,
            'kehadiran':update_absen.kehadiran,
            'keterangan':update_absen.keterangan,
            'Mapel':update_absen.Mapel,
    }
    FormAbsensi = InputAbsensi(request.POST or None,initial=data,instance=update_absen)
    if request.method == 'POST':
        if FormAbsensi.is_valid():
            FormAbsensi.save()
            return redirect('dashboardguru:tampilabsen')


    context={
        'absen' : FormAbsensi
    }
    return render(request,'absensi.html',context)



