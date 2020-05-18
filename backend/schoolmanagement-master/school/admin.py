from django.contrib import admin
from .models import *
# Register your models here. (by sumit.luv)

admin.site.register([Campus, Classes, Major, Teacher, Student, ChangeMajor, StudyDelay, Course, StartedCourseInfo, ChooseCourse])
