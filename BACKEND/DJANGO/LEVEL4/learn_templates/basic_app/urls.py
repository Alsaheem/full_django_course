from django.conf.urls import url
from basic_app import views
from django.urls import path

#TEMPLATE TAGGGING
app_name = 'basic_app'

urlpatterns = [
    path('other/', views.other,name='other'),
    path('relative/' ,views.relative,name='relative'),
]
