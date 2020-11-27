from django.shortcuts import render, HttpResponse
from .models import *
from .serializers import *
from rest_framework.renderers import JSONRenderer
# Create your views here.
def student(request,pk):
    student_obj = Student.objects.get(id=pk)
    serializer = StudentSerializer(student_obj)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type  = 'application/json')