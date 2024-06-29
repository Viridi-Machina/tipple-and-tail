"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from hello_world import views as index_views
from booking import views as booking_views
from user import views as use_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('booking/', booking_views.booking_page, name='booking'),
    # path('hello_world/', index_views.index, name='index'),
    path('summernote/', include('django_summernote.urls')),
    # path('user/', use_views.user_page, name='user'),
    path('', include('about.urls'), name='about-urls'),
]
