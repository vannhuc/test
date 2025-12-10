from django.db import models

# Create your models here.
class Khoa(models.Model):
    ma_khoa = models.AutoField(primary_key=True)
    ten_khoa = models.CharField(max_length=500)

class SinhVien(models.Model):
    ma_sv = models.AutoField(primary_key=True)
    ten_sv = models.CharField(max_length=500)
    gioi_tinh = models.BooleanField()
    ngay_sinh = models.DateField()
    #ma_khoa = models.ForeignKey(Khoa, on_delete=models.CASCADE)
    khoa =  models.CharField(max_length=500)
    #image_name = models.ImageField(upload_to='images/', null=True, blank=True)
    image_name = models.CharField(max_length=500)