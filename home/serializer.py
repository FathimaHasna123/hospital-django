from rest_framework import serializers
from .models import *



class ContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Contact
        fields = '__all__'
        
        
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class DepartmentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

        
        
class DoctorsSerializer(serializers.ModelSerializer):
   department = DepartmentSerializer()
   file_name = serializers.SerializerMethodField()
   class Meta:
        model=Doctors
        fields = '__all__'
   def get_file_name(self, obj):
        return obj.image.name if obj.image else None

class DoctorsPostSerializer(serializers.ModelSerializer):  
   class Meta:
        model=Doctors
        fields = '__all__'            
        
     
class AppointmentSerializer(serializers.ModelSerializer):
     department = DepartmentSerializer() 
     doctors = DoctorsSerializer()
    
     class Meta:
        model=Appointment
        fields = '__all__'                       
        