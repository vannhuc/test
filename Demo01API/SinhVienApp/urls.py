from django.urls import re_path
from SinhVienApp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    re_path(r'^khoa$', views.KhoaApi),
    re_path(r'^khoa/([0-9]+)$', views.KhoaApi),
    re_path(r'^sinhvien$', views.SinhVienApi),
    re_path(r'^sinhvien/([0-9]+)$', views.SinhVienApi),
    re_path(r'^sinhvien/SaveFile$', views.SaveFile)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)