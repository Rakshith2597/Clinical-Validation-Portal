from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('CT/', views.XR_func, name='CT'),
	path('MR/', views.XR_func, name='MR'),
	path('XR/', views.XR_func, name='XR'),


]
