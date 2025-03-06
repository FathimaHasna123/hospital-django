from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serialaizer import *
from rest_framework import status
from rest_framework.permissions import AllowAny

# Create your views here.
class ContactApi(APIView):
    def get(self, request):
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class DepartmentApi(APIView):
    def get(self,request):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        