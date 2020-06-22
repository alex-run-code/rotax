from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_tax_info/', views.get_tax_info, name='get_tax_info'),
    path('companies/', views.companies, name='companies'),
    path('all_responses/', views.all_responses, name='all_responses'),
    path('clear_responses/', views.clear_responses, name='clear_responses'),
    path('clear_companies/', views.clear_companies, name='clear_companies'),
    
]
