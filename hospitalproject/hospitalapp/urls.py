from django.urls import path
from.import views

urlpatterns = [
    path('',views.index,name='home'),
    path('booking',views.booking,name='booking'),
    path('contact',views.contact,name='contact'),
    path('department',views.department,name='department'),
    path('about',views.about,name='about'),
    path('doctors',views.doctors,name='doctors'),
]