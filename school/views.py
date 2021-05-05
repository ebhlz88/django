from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import studentsdetail
from .serializers import studentsdetailSerializer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.http.response import JsonResponse

@api_view(['GET', 'POST', 'DELETE'])
def studentslist(request):
    if request.method == 'GET':
        tutorials = studentsdetail.objects.all()
        
        title = request.query_params.get('s_name', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        
        tutorials_serializer = studentsdetailSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = studentsdetailSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        





""""
class studentslist(APIView):
    
        def get(self,request):
            
                student1=studentsdetail.objects.all()
                serializer = studentsdetailSerializer(student1, many=True)
                return Response(serializer.data)
    
        

        def post(self):
            pass
class studentpost(APIView):
    def create(self,request):
            
                serializer = studentsdetailSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                return Response(serializer.data)"""
# from rest_framework import viewsets
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated

# class studentslist(viewsets.ModelViewSet):
#     authentication_classes = (BasicAuthentication,)
#     permission_classes = (IsAuthenticated,)
#     queryset = studentsdetail.objects.all()
#     serializer_class = studentsdetailSerializer

def home(request):

     return render(request,'home.html')