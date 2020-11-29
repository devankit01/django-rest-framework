from django.contrib import admin
from .models import Student_Table
# Register your models here.

# admin.site.register(Student_Table)

@admin.register(Student_Table)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','city']