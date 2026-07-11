from django.shortcuts import render
from django.http import HttpResponse
from numpy import generic
from .models import Course
from .serializers import CourseSerializer
from rest_framework.views import APIView, Response, viewsets

# Create your views here.
def hello_view(request):
    return HttpResponse("Course Management API is running")

class CourseListView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = CourseSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)

class CourseDetailView(APIView):
    def get(self, request, pk):
        course = Course.objects.get(pk=pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def put(self, request, pk):
        course = Course.objects.get(pk=pk)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        course = Course.objects.get(pk=pk)
        course.delete()
        return Response(status=204)
    
class CourseViewList(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer