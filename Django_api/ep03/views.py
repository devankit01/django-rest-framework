from io import BytesIO

from django.shortcuts import HttpResponse, render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Student_Table
from .serializers import StudentSerializer


@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        stream = BytesIO(request.body)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)

        if id is not None:
            stu = Student_Table.objects.get(id=id)
            serializer = StudentSerializer(stu)

        else:
            stu = Student_Table.objects.all()
            # For all data attributes should be many = True
            serializer = StudentSerializer(stu, many=True)

        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'POST':

        stream = BytesIO(request.body)
        data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data inserted'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        else:
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type='application/json')

    if request.method == 'PUT':
        stream = BytesIO(request.body)
        data = JSONParser().parse(stream)
        id = data.get('id')
        stu = Student_Table.objects.get(id=id)

        # For Partial Update
        # serializer = StudentSerializer(stu, data=data, partial=True)

        # For complete update
        serializer = StudentSerializer(stu, data=data)

        if serializer.is_valid():
             serializer.save()
             res = {'msg': 'Data Updated'}
             json_data = JSONRenderer().render(res)
             return HttpResponse(json_data, content_type='application/json')
        else:
             json_data = JSONRenderer().render(serializer.errors)
             return HttpResponse(json_data, content_type='application/json')

    if request.method == 'DELETE':
        stream = BytesIO(request.body)
        data = JSONParser().parse(stream)
        id = data.get('id')
        stu = Student_Table.objects.get(id=id)
        stu.delete()
        res = {'msg': 'Data Deleted'}

        ''' You can also use => 
        return JsonResponse(res, safe = False) '''
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')