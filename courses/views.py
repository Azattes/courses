from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from . import serializers
from rest_framework import status
from .models import Course, Branch, Contact
from .serializers import CourseSerializers, BranchSerializers, ContactSerializers, CategorySerializers

class CourseAPIView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializers(courses, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetailAPIView(APIView):
    def get(self, request, pk, format=None):
        course = Course.objects.get(pk=pk)
        serializer = CourseSerializers(course)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        course = Course.objects.get(pk=pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        course = Course.objects.get(pk=pk)
        serializer = serializers.CourseSerializers(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
