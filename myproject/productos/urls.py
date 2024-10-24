from django.urls import path
from . import views

urlpatterns = [
    path('fabricas-y-productos/', views.obtener_fabricas_y_productos, name='fabricas_y_productos'),
]