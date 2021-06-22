from django.contrib import admin

# Register your models here.
from .models import Student
from .models import Employee
from .models import Contact_us

admin.site.register(Student)
admin.site.register(Employee)
admin.site.register(Contact_us)