from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import studentsdetail,yearclass,months,teacherdetail
from .serializers import studentsdetailSerializer,yearsSerializer,monthsSerializer,teacherdetailSerializer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.generics import ListAPIView
from rest_framework import generics
# from rest_framework.filters import SearchFilter
from rest_framework.filters import SearchFilter

@api_view(['GET', 'POST', 'DELETE'])
def studentslist(request):
    if request.method == 'GET':
        allstudents = studentsdetail.objects.all()
        
        title = request.query_params.get('s_name', None)
        if title is not None:
            allstudents = allstudents.filter(title__icontains=title)
        
        allstudents_serializer = studentsdetailSerializer(allstudents, many=True)
        return JsonResponse(allstudents_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        students_data = JSONParser().parse(request)
        allstudents_serializer = studentsdetailSerializer(data=students_data)
        if allstudents_serializer.is_valid():
            allstudents_serializer.save()
            return JsonResponse(allstudents_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(allstudents_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    elif request.method == 'DELETE':      
                studentsdetail.objects.all().delete()  
            
    return JsonResponse({'message':'all students data deleted'},status=status.HTTP_204_NO_CONTENT)
             
     
@api_view(['GET','POST','DELETE'])    
def studentdetail(request, pk) :    
        try:
            student=studentsdetail.objects.filter(pk=pk)
        except studentsdetail.DoesNotExist: 
            return JsonResponse({'message': 'The Student does not exist'}, status=status.HTTP_404_NOT_FOUND)
     
     
        if request.method == 'DELETE':
            student.delete()
            return JsonResponse({'message':'this row is deleted successfully'},status=status.HTTP_204_NO_CONTENT)
        elif request.method == 'GET':
            student=studentsdetail.objects.get(pk=pk)
            student_serializer=studentsdetailSerializer(student)
        return JsonResponse(student_serializer.data)

class sear(ListAPIView):
        queryset=studentsdetail.objects.all()
        serializer_class=studentsdetailSerializer
        filter_backends=[SearchFilter]
        search_fields=['s_name','s_fname','s_email','m_number']
    
        

@api_view(['GET', 'POST', 'DELETE'])
def yearview(request):
    if request.method == 'GET':
        yearr = yearclass.objects.all()
        years_serializer = yearsSerializer(yearr, many=True)
        return JsonResponse(years_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        year_data = JSONParser().parse(request)
        years_serializer = yearsSerializer(data=year_data)
        if years_serializer.is_valid():
            years_serializer.save()
            return JsonResponse(years_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(years_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    elif request.method == 'DELETE':      
                yearclass.objects.all().delete()  
            
    return JsonResponse({'message':'all students data deleted'},status=status.HTTP_204_NO_CONTENT)
    
    
@api_view(['GET'])
def monthsview(request,nam):
    if request.method == 'GET':
        monthss = months.objects.filter(student__s_name=nam)
        month_serializer = monthsSerializer(monthss, many=True)
        return JsonResponse(month_serializer.data, safe=False)
        # 'safe=False' for objects serialization



@api_view(['POST'])
def updateview(request,nam,yerr):
    monthss = months.objects.get(student__s_name=nam,years__year=yerr)
    if request.method == 'POST':
        data_month = JSONParser().parse(request)
        month_serializer = monthsSerializer(monthss, data=data_month, partial=True)
        if month_serializer.is_valid():
            month_serializer.save()
            return JsonResponse(month_serializer.data,status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(month_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    return JsonResponse({'message': 'The Student does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
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


class searchteacher(ListAPIView):
        queryset=teacherdetail.objects.all()
        serializer_class=teacherdetailSerializer
        filter_backends=[SearchFilter]
        search_fields=['t_name','t_fname','s_email','m_number','sex']
   
    
   
   
   
    # elif request.method == 'POST':
    #     month_data = JSONParser().parse(request)
    #     month_serializer = monthsSerializer(data=month_data)
    #     if month_serializer.is_valid():
    #         month_serializer.save()
    #         return JsonResponse(month_serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return JsonResponse(month_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    # elif request.method == 'DELETE':      
    #            months.objects.all().delete()  
            
    # return JsonResponse({'message':'all students data deleted'},status=status.HTTP_204_NO_CONTENT)
    #this is test for github commit
   


def home(request):

     return render(request,'home.html')