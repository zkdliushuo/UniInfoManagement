"""
by sumit kumar
written by fb.com/sumit.luv

"""
from django.contrib import admin
from django.urls import path
from school import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.home_view, name=''),

    path('major', views.major_view, name='major'),
    path('update-major/<pk>', views.update_major_view, name='update-major'),
    path('add-major', views.add_major_view, name='add-major'),
    path('delete-major/<pk>', views.delete_major_view, name='delete-major'),


    path('campus', views.campus_view, name='campus'),
    path('update-campus/<pk>', views.update_campus_view, name='update-campus'),
    path('add-campus', views.add_campus_view, name='add-campus'),
    path('delete-campus/<pk>', views.delete_campus_view, name='delete-campus'),

    path('classes', views.classes_view, name='classes'),
    path('update-classes/<pk>', views.update_classes_view, name='update-classes'),
    path('add-classes', views.add_classes_view, name='add-classes'),
    path('delete-classes/<pk>', views.delete_classes_view, name='delete-classes'),

    path('teacher', views.teacher_view, name='teacher'),
    path('update-teacher/<pk>', views.update_teacher_view, name='update-teacher'),
    path('add-teacher', views.add_teacher_view, name='add-teacher'),
    path('delete-teacher/<pk>', views.delete_teacher_view, name='delete-teacher'),

    path('student', views.student_view, name='student'),
    path('update-student/<pk>', views.update_student_view, name='update-student'),
    path('add-student', views.add_student_view, name='add-student'),
    path('delete-student/<pk>', views.delete_student_view, name='delete-student'),

    path('study-delay-event', views.study_delay_event_view, name='study-delay-event'),
    path('update-study-delay-event/<pk>', views.update_study_delay_event_view, name='update-study-delay-event'),
    path('add-study-delay-event', views.add_study_delay_event_view, name='add-study-delay-event'),
    path('delete-study-delay-event/<pk>', views.delete_study_delay_event_view, name='delete-study-delay-event'),

    path('change-major-event', views.change_major_event_view, name='change-major-event'),
    path('update-change-major-event/<pk>', views.update_change_major_event_view, name='update-change-major-event'),
    path('add-change-major-event', views.add_change_major_event_view, name='add-change-major-event'),
    path('delete-change-major-event/<pk>', views.delete_change_major_event_view, name='delete-change-major-event'),

    path('course', views.course_view, name='course'),
    path('update-course/<pk>', views.update_course_view, name='update-course'),
    path('add-course', views.add_course_view, name='add-course'),
    path('delete-course/<pk>', views.delete_course_view, name='delete-course'),

    path('started-course', views.started_course_view, name='started-course'),
    path('update-started-course/<pk>', views.update_started_course_view, name='update-started-course'),
    path('add-started-course', views.add_started_course_view, name='add-started-course'),
    path('delete-started-course/<pk>', views.delete_started_course_view, name='delete-started-course'),

    path('select-course', views.select_course_view, name='select-course'),
    path('update-select-course/<pk>', views.update_select_course_view, name='update-select-course'),
    path('add-select-course', views.add_select_course_view, name='add-select-course'),
    path('delete-select-course/<pk>', views.delete_select_course_view, name='delete-select-course'),

]
