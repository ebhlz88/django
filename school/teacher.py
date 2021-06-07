from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import yearclass,teacherdetail,teachpaymonths
from .serializers import yearsSerializer,teacherdetailSerializer,t_paymentSerializer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.generics import ListAPIView
from rest_framework import generics
from rest_framework.filters import SearchFilter


@api_view(['GET','POST'])
def teacheroverall(request):
    if request.method == 'GET':
        allteacherdetail = teacherdetail.objects.filter()
        allteacherserializer = teacherdetailSerializer(allteacherdetail,many=True)
        return JsonResponse(allteacherserializer.data,safe=False)
    elif request.method == 'POST':
        teacherpostdata = JSONParser().parse(request)
        postserializer = teacherdetailSerializer(data=teacherpostdata)
        if postserializer.is_valid():
            postserializer.save()
            return JsonResponse(postserializer.data,status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({'message': 'invalid entry'},status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':      
                teacherdetail.objects.all().delete()  
            
    return JsonResponse({'message':'all students data deleted'},status=status.HTTP_204_NO_CONTENT)


class searchteacher(ListAPIView):
        queryset=teacherdetail.objects.all()
        serializer_class=teacherdetailSerializer
        filter_backends=[SearchFilter]
        search_fields=['t_name','t_fname','s_email','m_number','sex']
   
@api_view(['GET'])
def teacherpaymentview(request,tnam):
    if request.method == 'GET':
        monthss = teachpaymonths.objects.filter(teacher__t_name=tnam)
    
        month_serializer = t_paymentSerializer(monthss ,many=True)
        return JsonResponse(month_serializer.data, safe=False)   
   
@api_view(['POST'])
def updateteacherpayments(request,tnam,tyear,pk):
    if request.method == 'POST':
        if tnam != 'null':
            tmonthss = teacherdetail.objects.get(t_name=tnam)
        yearr = yearclass.objects.get(year=tyear)
        data_month = JSONParser().parse(request)
        try:
            if pk != 0:
                monthss = teachpaymonths.objects.get(teacher__pk=pk,years__year=tyear)
            else:
                    monthss = teachpaymonths.objects.get(teacher__t_name=tnam,years__year=tyear)
            tmonth_serializer = t_paymentSerializer(monthss, data=data_month, partial=True)
            if tmonth_serializer.is_valid():
                tmonth_serializer.save()
                return JsonResponse(tmonth_serializer.data,status=status.HTTP_201_CREATED)
            else:
                return JsonResponse(month_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except teachpaymonths.DoesNotExist:
            ins = teachpaymonths(teacher=tmonthss,years=yearr)
            ins.save()
            monthss = teachpaymonths.objects.get(teacher__t_name=tnam,years__year=tyear)
            tmonth_serializer = t_paymentSerializer(monthss,data=data_month, partial=True)
            if tmonth_serializer.is_valid():
                tmonth_serializer.save()
                return JsonResponse(tmonth_serializer.data,status=status.HTTP_201_CREATED)
            else:
                return JsonResponse(tmonth_serializer.errors, status=status.HTTP_400_BAD_REQUEST)