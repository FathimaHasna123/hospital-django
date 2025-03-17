from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from rest_framework import status
from rest_framework.permissions import AllowAny

# Create your views here.
class ContactApi(APIView):
    permission_classes=[AllowAny]
    def get(self, request):
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ContactPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
        
    
    
class DepartmentApi(APIView):
    permission_classes=[AllowAny]
    def get(self,request):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
      
        serializer =DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,id=None):
        department = Department.objects.get(id=id)
        print("printing :::::::::::" , request.data)
        serializer = DepartmentPostSerializer(department,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id=None):
        department = Department.objects.get(id=id)
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class DoctorsApi(APIView):
    permission_classes=[AllowAny]
    def get(self,request):
        doctors = Doctors.objects.all()
        serializer = DoctorsSerializer(doctors,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = DoctorsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,id=None):
        doctors = Doctors.objects.get(id=id)
        
        serializer = DoctorsPostSerializer(doctors,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self,request,id=None):
        doctros = Doctors.objects.get(id=id)
        doctros.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 

    
    
    
    
class AppointmentApi(APIView):
    permission_classes=[AllowAny]
    def get(self,request):
        appointment = Appointment.objects.all()
        serializer = AppointmentSerializer(appointment, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def post(self,request):
        serializer = AppointmentPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     
        
        
        
        
        
        
        
        
        
        
        