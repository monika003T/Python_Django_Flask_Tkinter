from django.urls import path 
from test_app import views

urlpatterns=[
    path('', views.home, name='home'),
    path('web.html', views.web, name='web'),
    path('form.html', views.form, name='form')
]
