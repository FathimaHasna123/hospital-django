from rest_framework import serializers
from .models import *



class ContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Contact
        fields = '__all__'
        
        
class DepartmentSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model=Department
        fields = '__all__'
        
        
class DoctorsSerializer(serializers.ModelSerializer):
   department = DepartmentSerializer()
    
class Meta:
        model=Doctors
        fields = '__all__'
        
     
class AppointmentSerializer(serializers.ModelSerializer):
     department = DepartmentSerializer() 
     doctors = DoctorsSerializer()
    
class Meta:
        model=Appointment
        fields = '__all__'                       
        