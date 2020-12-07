"""miriadvtt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from homeapp import views as homeviews
from vttapp import views as vttappviews
from dashboard import views as dashboardviews
from WP3 import views as wp3views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wp1/', vttappviews.index, name='index1'),
    path('home/',homeviews.index, name='index'),
    path('WP1/',homeviews.WP1, name='WP1'),
    path('WP3/',homeviews.WP3, name='WP3'),
    path('wp3/',wp3views.index, name='index2'),
    path('CT_test', vttappviews.CT_func, name='CT_test'),
    path('MR_test', vttappviews.MR_func, name='MR_test'),
    path('XR_test', vttappviews.XR_func, name='XR_test'),
    path('wp3_test', wp3views.wp3_test, name='wp3_test'),
    path('register/', vttappviews.register_user, name='register'),
    path('dashboard/', dashboardviews.dashboard, name='dashboard'),
    path('dashboard_admin/', dashboardviews.dashboard_admin, name='dashboard_admin'),
    path('dashboard_admin_wp1/', dashboardviews.dashboard_admin_wp1, name='dashboard_admin_wp1'),
    path('dashboard_admin_wp3/', dashboardviews.dashboard_admin_wp3, name='dashboard_admin_wp3'),
    path('export_csv_wp3/', wp3views.export_csv_wp3, name='export_csv_wp3'),
    path('export_csv_wp1/', vttappviews.export_csv_wp1, name='export_csv_wp1'),
    # path('response/', views.detail_response_func, name='RF'),
    # path('response/', vttappviews.response_func, name='RF'),
    path('', RedirectView.as_view(url='home/')),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
