from django.urls import path
from .views import display_toy_data  

urlpatterns = [
    path('toys/', display_toy_data, name='display_toy_data'),
]