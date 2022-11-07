from django.urls import path

from . import views


app_name = 'products'
urlpatterns = [
    path('', views.ProductsView.as_view(), name='home'),
    path('seedbox/<slug>', views.SeedBoxView.as_view(), name='seedbox'),
]