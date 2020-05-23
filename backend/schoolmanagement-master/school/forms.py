from django import forms
from . import models


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
        model = models.Teacher
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
        exclude = ['teachers']


class StartedCourseInfoForm(forms.ModelForm):
    class Meta:
        model = models.StartedCourseInfo
        fields = '__all__'


class TobeChangedStartedCourseInfoForm(forms.ModelForm):
    class Meta:
        model = models.StartedCourseInfo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['year_start'].widget.attrs['readonly'] = True
        self.fields['semester_start'].widget.attrs['readonly'] = True
        self.fields['day_start'].widget.attrs['readonly'] = True
        self.fields['when_start'].widget.attrs['readonly'] = True
        self.fields['course'].widget.attrs['readonly'] = True


class ChooseCourseForm(forms.ModelForm):
    class Meta:
        model = models.ChooseCourse
        fields = '__all__'
