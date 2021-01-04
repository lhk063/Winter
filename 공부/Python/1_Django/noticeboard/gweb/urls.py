from django.urls import path
from gweb import views

urlpatterns = [
    path('', views.index, name='index'),
]
