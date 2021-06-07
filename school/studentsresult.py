from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from .serializers import studentsresultSerializer,subjectsSerializer,standardSerializer
from .models import marks,studentsdetail,yearclass,subjects,schoolclasses
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http import HttpResponse
from django.shortcuts import get_object_or_404



@api_view(['GET'])
def getstudentresult(request,sroll):
    if request.method == 'GET':
        student = marks.objects.filter(student__rollnbr=sroll)
        # print(student.standard)
        studentresultSerializer = studentsresultSerializer(student,many = True)
        return JsonResponse(studentresultSerializer.data,safe= False)

@api_view(['POST'])
def postresult(request,sroll,year,subject,sstandard):
    # {% csrf %}
    if request.method == 'POST':
        try:
            smark = marks.objects.get(student__rollnbr=sroll,years__year=year,subjectname__subjectname=subject,standard__standardname=sstandard)
            return JsonResponse({'message':'Result already exists do you want to overide'},status=status.HTTP_400_BAD_REQUEST)
        except marks.DoesNotExist:
            student=studentsdetail.objects.get(rollnbr=sroll)
            yearcls = yearclass.objects.get(year=year)
            subject=subjects.objects.get(subjectname=subject)
            standard = schoolclasses.objects.get(standardname=sstandard)
            ins = marks(student=student,years=yearcls,standard=standard,subjectname=subject,subjectmarks=0)
            ins.save()
            smark = marks.objects.get(student__rollnbr=sroll,years__year=year,subjectname__subjectname=subject,standard__standardname=sstandard)
            result_data = JSONParser().parse(request)
            studentresultSerializer = studentsresultSerializer(smark,data=result_data,partial=True)
            if studentresultSerializer.is_valid():
                studentresultSerializer.save()
                return JsonResponse(studentresultSerializer.data,status=status.HTTP_201_CREATED)
            else:
                return JsonResponse(status=status.HTTP_400_BAD_REQUEST)
            
                
        # if smark is not None:

        #     return JsonResponse({'message':'Result already exists do you want to overide'},status=status.HTTP_400_BAD_REQUEST)
        # except marks.DoesNotExist:
        # elif smark is None:
           
            

@api_view(['GET'])
def getsubjects(request):
    if request.method == 'GET':
        allsubjects = subjects.objects.all()
        subjectserializer = subjectsSerializer(allsubjects,many= True)
        return JsonResponse(subjectserializer.data,safe=False)


@api_view(['GET'])
def getstandards(request):
    if request.method == 'GET':
        allstandards = schoolclasses.objects.all()
        standards = standardSerializer(allstandards,many= True)
        return JsonResponse(standards.data,safe=False)


@api_view(['GET'])
def getstandardsbyid(request):
    if request.method == 'GET':
        allstandards = schoolclasses.objects.all()
        standards = standardSerializer(allstandards,many= True)
        return JsonResponse(standards.data,safe=False)

@api_view(['GET'])
def getsubjectsbyid(request,pk):
    if request.method == 'GET':
        allsubjects = subjects.objects.get(pk)
        subjectserializer = subjectsSerializer(allsubjects,many= True)
        return JsonResponse(subjectserializer.data,safe=False)

    

