"""
URL configuration for task_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
    path('data/<str:key>/', views.data_lookup, name='data_lookup'),
    path('update-data/', views.update_data, name='update_data'),
    path('data/item/<int:item_id>/', views.cached_data, name='cached_data'),
    path('restricted-area/', views.restricted_area, name='restricted_area'),
    path('validate-json/', views.validate_json, name='validate_json'),
    path('check-device/', views.check_device, name='check_device'),
    path('mobile-page/', views.mobile_page, name='mobile_page'),
]
