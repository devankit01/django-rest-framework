from django.shortcuts import render, HttpResponse
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from io import BytesIO
# Create your views here.

@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        # json_data =  request.DATA
        stream = BytesIO(request.body)
        data = JSONParser().parse(stream)
        serializer = StudentSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg' : 'Data inserted'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = 'application/json')
        else:
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type = 'application/json')
