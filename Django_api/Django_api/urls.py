
from django.contrib import admin
from django.urls import path
from ep01.views import student

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stu_detail/<pk>/', student,  name = "student"),

]
