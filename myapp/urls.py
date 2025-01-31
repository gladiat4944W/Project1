from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pizzas', views.pizzas, name='pizzas'),
    path('deals', views.deals, name='deals'),
    path('orders', views.orders, name='orders'),    # New path for pizzas
    # Add more paths for additional HTML files here
]
