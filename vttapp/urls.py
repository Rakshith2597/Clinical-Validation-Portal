from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('CT/', views.VTTApp.as_view(), name='CT'),
	path('MR/', views.VTTApp.as_view(), name='MR'),
	path('XR/', views.XR_func, name='XR'),


]
