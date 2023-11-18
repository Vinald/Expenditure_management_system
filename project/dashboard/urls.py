from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard-index'),
    path('index/', views.index, name='dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('item/', views.item, name='dashboard-item'),
    path('quantity/', views.quantity, name='dashboard-quantity'),
    
]
