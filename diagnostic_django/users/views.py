import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from users.serializers import UserSerializer,CustomerSerializer ,EmployeeSerializer
from .models import User , Customer
# Create your views here.

# @api_view(['POST','PUT'])
# def registerCustomer(request):
#     if request.method == 'POST':
#         print(request.data)
#         print(request)
#         # data = json.parse(request)

#         serializer = UserSerializer(data = request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             customer_obj = CustomerSerializer(data = {"customer_id":"MEDC"+str(user.id),"user_id":user.id})
#             if customer_obj.is_valid():
#                 customer_obj.save()

#             return Response(serializer.data)
#         # print(user_obj)
#         # print(serializer)
#     return Response({"msg":"not created"},status =400)


class RegisterCustomer(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            user = serializer.save()
            customer_obj = CustomerSerializer(data = {"customer_id":"MEDC"+str(user.id),"user_id":user.id})
            if customer_obj.is_valid():
                customer_obj.save()
            else:
                print('invalid')
                return Response(customer_obj.errors, status=status.HTTP_400_BAD_REQUEST) 
            return Response(customer_obj.data,status=200)
        else:
            print('invalid')
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


class RegisterEmployee(APIView):
    def post(self,request):
        print(request.data)
        serializer = UserSerializer(data={'username': request.data["username"],"first_name":request.data["first_name"],'last_name':request.data["last_name"],'email':request.data['email'],"mobile_number":request.data["mobile_number"],"age":request.data['age'],'address':request.data['address'],"pincode":request.data['pincode'] , "password":request.data['password']})
        print(serializer)
        if serializer.is_valid():
            user = serializer.save()
            employee_obj = EmployeeSerializer(data = {"staff_id":"MEDS"+str(user.id),"user_id":user.id ,"designation":request.data["designation"] , "qualification":request.data['qualification'],"salary":request.data['salary'],"years_of_experience":request.data['years_of_experience'] or None, 'branch':request.data['branch'], "status":request.data['status'] })
            if employee_obj.is_valid():
                employee_obj.save()
            else:
                return Response(employee_obj.errors, status=status.HTTP_400_BAD_REQUEST)   
            return Response(employee_obj.data,status=200)
        else:
            print('invalid')
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


