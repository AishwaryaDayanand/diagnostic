from dataclasses import field
from rest_framework import serializers
from  .models import Customer, User


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','is_staff','mobile_number','age','address','pincode']

        