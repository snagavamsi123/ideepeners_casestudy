from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('signup/',views.exe_signup,name='signup'),
    path('login/',views.login,name='login'),
    path('dailyupdate/',views.dailyupdate,name='dailyupdate'),
    path('clientdetails/',views.clientdetails,name='clientdetails'),
    path('clientreport/',views.clientreport_page,name='clientreport'),
    path('dailyreport/',views.dailyreport_page,name='dailyreport')
]