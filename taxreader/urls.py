from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_tax_info', views.get_tax_info, name='get_tax_info'),
    path('companies', views.companies, name='companies'),
]
