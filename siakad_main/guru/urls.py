from django.urls import path
from django.urls.conf import include
from . import views as viewsGuru
urlpatterns = [
path('',viewsGuru.dashboardguru,name='dashboardguru'),
path('carts',viewsGuru.dasboardcart,name='dashboardchart'),
path('tabel',viewsGuru.dasboardtables,name='dashboardtable'),
path('absensi',viewsGuru.absensi,name='absensi'),
path('jadwal',viewsGuru.jadwal,name='jadwal'),
path('forbidden',viewsGuru.forbidden,name='forbidden'),
path('tampilabsen',viewsGuru.tampilabsen,name='tampilabsen'),
path('inputnilai',viewsGuru.inputnilai,name='inputnilai'),
path('hapus/?P<delid>',viewsGuru.hapusabsen,name='hapusabsen'),
path('edit/?P<editid>',viewsGuru.editabsen,name='editabsen')
]