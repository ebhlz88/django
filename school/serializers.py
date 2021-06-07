from rest_framework import serializers
from django.contrib.auth.models import User
from .models import studentsdetail,yearclass,months,teacherdetail,teachpaymonths,marks,subjects,schoolclasses

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

class studentsresultSerializer(serializers.ModelSerializer):

    class Meta: 
        model = marks
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['standard'] = standardSerializer(instance.standard).data 
        rep['subjectname'] = subjectsSerializer(instance.subjectname).data
        return rep

    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)
    #     rep['subjectname'] = subjectsSerializer(instance.subjectname).data
    #     return rep
    

class subjectsSerializer(serializers.ModelSerializer):

    class Meta:
        model = subjects
        fields = '__all__'

class standardSerializer(serializers.ModelSerializer):
    class Meta:
        model = schoolclasses
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user