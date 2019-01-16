from basicapp import views
from django.urls import path

urlpatterns=[
    path('',views.form_name_view,name='form_name'),

]
