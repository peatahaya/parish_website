from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', views.test_page, name='test_page'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
