from django.shortcuts import render, HttpResponse
from .models import *
from .serializers import *
from rest_framework.renderers import JSONRenderer
# Create your views here.
def student(request,pk):
    student_obj = Student.objects.get(id=pk) # Get data
    serializer = StudentSerializer(student_obj) # Serialize
    json_data = JSONRenderer().render(serializer.data) # convert to json
    '''return HttpResponse (serializer.data) => You can use this as well '''
    return HttpResponse(json_data, content_type  = 'application/json') # returning response




def student_list(request):
    student_obj = Student.objects.all() # Get data
    print(student_obj)
    serializer = StudentSerializer(student_obj ,many = True) # Serialize
    print(serializer)
    json_data = JSONRenderer().render(serializer.data) # convert to json
    '''return HttpResponse(serializer.data)'''
    return HttpResponse(json_data, content_type  = 'application/json') # returning response