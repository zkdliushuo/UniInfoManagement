from django import forms
from django.contrib.auth.models import User
from . import models


# for admin
class AdminSigupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']


# for student related form
class StudentUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']


class StudentExtraForm(forms.ModelForm):
    class Meta:
        model = models.StudentExtra
        fields = ['roll', 'cl', 'mobile', 'fee', 'status']


# for teacher related form
class TeacherUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']


class TeacherExtraForm(forms.ModelForm):
    class Meta:
        model = models.TeacherExtra
        fields = ['salary', 'mobile', 'status']


# for Attendance related form
presence_choices = (('Present', 'Present'), ('Absent', 'Absent'))


class AttendanceForm(forms.Form):
    present_status = forms.ChoiceField(choices=presence_choices)
    date = forms.DateField()


class AskDateForm(forms.Form):
    date = forms.DateField()


# for notice related form
class NoticeForm(forms.ModelForm):
    class Meta:
        model = models.Notice
        fields = '__all__'


# for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))


class CampusForm(forms.ModelForm):
    class Meta:
        model = models.Campus
        fields = '__all__'


class MajorForm(forms.ModelForm):
    class Meta:
        model = models.Major
        fields = '__all__'


class ClassesForm(forms.ModelForm):
    class Meta:
        model = models.Classes
        fields = '__all__'


class PeopleForm(forms.ModelForm):
    class Meta:
        model = models.People
        fields = '__all__'


class TeacherForm(forms.ModelForm):
    class Meta:
        model = models.Notice
        fields = '__all__'


class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = '__all__'


class StudyEventForm(forms.ModelForm):
    class Meta:
        model = models.StudyEvent
        fields = '__all__'


class ChangeMajorForm(forms.ModelForm):
    class Meta:
        model = models.ChangeMajor
        fields = '__all__'


class StudyDelayForm(forms.ModelForm):
    class Meta:
        model = models.StudyDelay
        fields = '__all__'


class CourseForm(forms.ModelForm):
    class Meta:
        model = models.Course
        fields = '__all__'


class StartedCourseInfoForm(forms.ModelForm):
    class Meta:
        model = models.StartedCourseInfo
        fields = '__all__'


class ChooseCourseForm(forms.ModelForm):
    class Meta:
        model = models.ChooseCourse
        fields = '__all__'
