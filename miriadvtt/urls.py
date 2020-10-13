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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vttapp/', vttappviews.index, name='index1'),
    path('homeapp/',homeviews.index, name='index'),
    path('WP1/',homeviews.WP1, name='WP1'),
    path('CT_test', vttappviews.CT_func, name='CT_test'),
    path('MR_test', vttappviews.MR_func, name='MR_test'),
    path('XR_test', vttappviews.XR_func, name='XR_test'),
    path('register/', vttappviews.register_user, name='register'),
    path('dashboard/', vttappviews.dashboard, name='dashboard'),
    # path('response/', views.detail_response_func, name='RF'),
    path('response/', vttappviews.response_func, name='RF'),
    path('', RedirectView.as_view(url='homeapp/')),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
