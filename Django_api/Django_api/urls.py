
from django.contrib import admin
from django.urls import path
from ep01.views import student,student_list
from ep02.views import student_create
from ep03.views import student_api

urlpatterns = [
    path('admin/', admin.site.urls),

    # Ep01 urls
    path('ep1/stu_detail/<pk>/', student,  name = "student"),
    path('ep1/stu_list/', student_list,  name = "student_list"),

    # Ep02 urls
    path('ep2/stu_create/', student_create,  name = "student_create"),

    # Ep03 urls
    path('ep3/stu_api/', student_api,  name = "student_api"),



]
