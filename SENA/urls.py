from django.urls import path
from . import views

urlpatterns = [
    path('aprendices/', views.lista_aprendices, name='lista_aprendices'),
]

urlpatterns = [
    path('', views.lista_aprendices, name='inicio'),
    path('aprendices/', views.lista_aprendices, name='lista_aprendices'),
]