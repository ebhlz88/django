from django.contrib import admin
from school.models import studentsdetail,yearclass,months,teacherdetail,teachpaymonths,subjects,marks,schoolclasses

# Register your models here.
admin.site.register(studentsdetail)
admin.site.register(yearclass)
admin.site.register(months)
admin.site.register(teacherdetail)
admin.site.register(teachpaymonths)
admin.site.register(schoolclasses)
admin.site.register(subjects)
admin.site.register(marks)
# admin.site.register(users)