from django.urls import path
from . import views
from user import views as user_views

urlpatterns = [
    path('', views.index, name='dashboard-index'),
    path('index/', views.index, name='dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('item/', views.item, name='dashboard-item'),
    path('quantity/', views.quantity, name='dashboard-quantity'),
    path('register/', user_views.register, name='user-register'),   
]
