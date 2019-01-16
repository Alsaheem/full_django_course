from django.urls import path
from app_two import views

urlpatterns = [
    path('', views.index,name='index2'),
]
