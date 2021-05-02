from django.urls import path
from . import views as viewsMurid
urlpatterns = [
path('',viewsMurid.dashboardmurid,name='dashboardmurid'),
]