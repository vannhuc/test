from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.core.files.storage import default_storage

from SinhVienApp.models import Khoa, SinhVien
from SinhVienApp.serializers import KhoaSerializer, SinhVienSerializer

@csrf_exempt
def KhoaApi(request, ma_khoa=0):
    if request.method=='GET':
        khoa = Khoa.objects.all()
        khoa_serializer = KhoaSerializer(khoa, many=True)
        return JsonResponse(khoa_serializer.data, safe=False)

    elif request.method=='POST':
        khoa_data = JSONParser().parse(request)
        khoa_serializer = KhoaSerializer(data=khoa_data)
        if khoa_serializer.is_valid():
            khoa_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)

    elif request.method=='PUT':
        khoa_data = JSONParser().parse(request)
        khoa = Khoa.objects.get(ma_khoa=khoa_data['ma_khoa'])
        khoa_serializer = KhoaSerializer(khoa, data=khoa_data)
        if khoa_serializer.is_valid():
            khoa_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)

    elif request.method=='DELETE':
        khoa = Khoa.objects.get(ma_khoa=ma_khoa)
        khoa.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def SinhVienApi(request, ma_sv=0):
    if request.method=='GET':
        sv = SinhVien.objects.all()
        sv_serializer = SinhVienSerializer(sv, many=True)
        return JsonResponse(sv_serializer.data, safe=False)

    elif request.method=='POST':
        sv_data = JSONParser().parse(request)
        sv_serializer = SinhVienSerializer(data=sv_data)
        if sv_serializer.is_valid():
            sv_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)

    elif request.method=='PUT':
        sv_data = JSONParser().parse(request)
        sv = SinhVien.objects.get(ma_sv=sv_data['ma_sv'])
        sv_serializer = SinhVienSerializer(sv, data=sv_data)
        if sv_serializer.is_valid():
            sv_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)

    elif request.method=='DELETE':
        sv = SinhVien.objects.get(ma_sv=ma_sv)
        sv.delete()
        return JsonResponse("Deleted Successfully", safe=False)
    
@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)
