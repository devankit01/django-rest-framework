
from django.contrib import admin
from django.urls import path
from ep01.views import student,student_list
from ep02.views import student_create

urlpatterns = [
    path('admin/', admin.site.urls),

    # Ep01 urls
    path('ep1/stu_detail/<pk>/', student,  name = "student"),
    path('ep1/stu_list/', student_list,  name = "student_list"),

    # Ep02 urls
    path('ep2/stu_create/', student_create,  name = "student_create"),


]
