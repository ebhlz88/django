from rest_framework import serializers
from .models import studentsdetail

class studentsdetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = studentsdetail
        #fields=['s_name',]
        fields = '__all__'
