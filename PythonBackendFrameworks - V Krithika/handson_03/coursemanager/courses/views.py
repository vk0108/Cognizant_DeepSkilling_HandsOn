from django.shortcuts import render
from django.http import HttpResponse
from .models import Course
from .serializers import CourseSerializer
from rest_framework.views import APIView, Response

# Create your views here.
def hello_view(request):
    return HttpResponse("Course Management API is running")

def CourseListView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        