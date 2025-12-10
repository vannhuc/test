from rest_framework import serializers
from SinhVienApp.models import Khoa, SinhVien

class KhoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Khoa
        fields = ('ma_khoa', 'ten_khoa')

class SinhVienSerializer(serializers.ModelSerializer):
    class Meta:
        model = SinhVien
        fields = ('ma_sv', 'ten_sv', 'gioi_tinh', 'ngay_sinh', 'khoa', 'image_name')