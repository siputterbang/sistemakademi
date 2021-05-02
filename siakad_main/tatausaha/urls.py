from django.urls import path
from . import views as ViewsTU

urlpatterns = [
    path('',ViewsTU.landingTU,name='TU'),
    path('login',ViewsTU.login,name='login'),

]
