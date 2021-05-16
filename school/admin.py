from django.contrib import admin
from school.models import studentsdetail,yearclass,months,teacherdetail

# Register your models here.
admin.site.register(studentsdetail)
admin.site.register(yearclass)
admin.site.register(months)
admin.site.register(teacherdetail)