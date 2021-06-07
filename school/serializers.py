from rest_framework import serializers
from .models import studentsdetail,yearclass,months,teacherdetail,teachpaymonths

class studentsdetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = studentsdetail
        #fields=['s_name',]
        fields = '__all__'

class yearsSerializer(serializers.ModelSerializer):

    class Meta:
        model = yearclass
        fields = '__all__'

class monthsSerializer(serializers.ModelSerializer):

    class Meta:
        model = months
        fields = '__all__'
        # fields = ['january','february','march','april','may','june','july','august','october','september'
        # ,'november','december','student']

class teacherdetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = teacherdetail
        fields = '__all__'

class t_paymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = teachpaymonths
        fields = '__all__'