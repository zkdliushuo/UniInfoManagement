from django.shortcuts import render, redirect
from . import forms, models
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db.models import ProtectedError
from django.contrib import messages


def home_view(request):
    return render(request, 'school/base.html')


def major_view(request):
    form = forms.MajorForm()
    majors = models.Major.objects.all()
    if request.method == 'POST':
        form = forms.MajorForm(request.POST)
        ret = {}
        for key, value in form.data.items():
            if value:
                ret[key] = value
        majors = models.Major.objects.filter(**ret)
    return render(request, 'school/major.html', context={'form': form, 'majors': majors})


def update_major_view(request, pk):
    try:
        major = models.Major.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return HttpResponseRedirect('major')
    if request.method == 'POST':
        form = forms.MajorForm(request.POST, instance=major)
        if 'id' in form.changed_data:
            form.errors.clear()
            form.errors['id'] = '错误，专业代码不可修改'
            return render(request, 'school/update_major.html', context={'form': form})
        if form.is_valid():
            form.save()
            return redirect('major')
    else:
        form = forms.MajorForm(instance=major)
    return render(request, 'school/update_major.html', context={'form': form})


def add_major_view(request):
    form = forms.MajorForm()
    if request.method == 'POST':
        form = forms.MajorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('major')
    return render(request, 'school/add_major.html', context={'form': form})


def delete_major_view(request, pk):
    try:
        major = models.Major.objects.get(pk=pk)
    except ObjectDoesNotExist:
        messages.error(request, '错误：不存在这个条目，不可删除')
    try:
        major.delete()
    except ProtectedError:
        messages.error(request, '错误：存在关联信息，不可删除')
    return redirect('major')


def campus_view(request):
    form = forms.CampusForm()
    campuses = models.Campus.objects.all()
    if request.method == 'POST':
        form = forms.CampusForm(request.POST)
        print(form.data)
        ret = {}
        for key, value in form.data.items():
            if value:
                print(key, value)
                ret[key] = value

        campuses = models.Campus.objects.filter(**ret)
    return render(request, 'school/campus.html', context={'form': form, 'campuses': campuses})


def update_campus_view(request, pk):
    try:
        campus = models.Campus.objects.get(pk=pk)
    except ObjectDoesNotExist:
        print("您想编辑的条目不存在.")
    if request.method == 'POST':
        form = forms.CampusForm(request.POST, instance=campus)
        if 'id' in form.changed_data:
            form.errors.clear()
            form.errors['id'] = '错误，校区代码不可修改'
            return render(request, 'school/update_campus.html', context={'form': form})
        if form.is_valid():
            form.save()
            return redirect('campus')
    else:
        form = forms.CampusForm(instance=campus)
    return render(request, 'school/update_campus.html', context={'form': form})


def add_campus_view(request):
    form = forms.CampusForm()
    if request.method == 'POST':
        form = forms.CampusForm(request.POST)
        if form.is_valid():
            form.save()
            # return 才能跳出当前方法 实现重定向
            return HttpResponseRedirect('campus')
    return render(request, 'school/add_campus.html', context={'form': form})


# 建议是否改成确定删除
def delete_campus_view(request, pk):
    try:
        campus = models.Campus.objects.get(pk=pk)
    except ObjectDoesNotExist:
        messages.error(request, '错误：不存在这个条目，不可删除')
    try:
        campus.delete()
    except ProtectedError:
        messages.error(request, '错误：存在关联信息，不可删除')
    return redirect('campus')


def classes_view(request):
    form = forms.ClassesForm()
    classes = models.Classes.objects.all()
    if request.method == 'POST':
        form = forms.ClassesForm(request.POST)
        print(form.data)
        ret = {}
        for key, value in form.data.items():
            if value:
                print(key, value)
                ret[key] = value

        classes = models.Classes.objects.filter(**ret)
    return render(request, 'school/classes.html', context={'form': form, 'classes': classes})


def update_classes_view(request, pk):
    try:
        classes = models.Classes.objects.get(pk=pk)
    except ObjectDoesNotExist:
        print("您想编辑的条目不存在.")
    if request.method == 'POST':
        form = forms.ClassesForm(request.POST, instance=classes)
        if 'id' in form.changed_data:
            form.errors.clear()
            form.errors['id'] = '错误，班级代码不可修改'
            return render(request, 'school/update_classes.html', context={'form': form})
        if form.is_valid():
            form.save()
            return redirect('classes')
    else:
        form = forms.ClassesForm(instance=classes)
    return render(request, 'school/update_classes.html', context={'form': form})


def add_classes_view(request):
    form = forms.ClassesForm()
    if request.method == 'POST':
        form = forms.ClassesForm(request.POST)
        if form.is_valid():
            form.save()
            # return 才能跳出当前方法 实现重定向
            return HttpResponseRedirect('class')
    return render(request, 'school/add_classes.html', context={'form': form})


# 建议是否改成确定删除
def delete_classes_view(request, pk):
    try:
        classes = models.Classes.objects.get(pk=pk)
    except ObjectDoesNotExist:
        messages.error(request, '错误：不存在这个条目，不可删除')
    try:
        classes.delete()
    except ProtectedError:
        messages.error(request, '错误：存在关联信息，不可删除')
    return redirect('classes')


def teacher_view(request):
    form = forms.TeacherForm()
    teachers = models.Teacher.objects.all()
    if request.method == 'POST':
        form = forms.TeacherForm(request.POST)
        print(form.data)
        ret = {}
        for key, value in form.data.items():
            if value:
                print(key, value)
                ret[key] = value

        teachers = models.Teacher.objects.filter(**ret)
    return render(request, 'school/teacher.html', context={'form': form, 'teachers': teachers})


def update_teacher_view(request, pk):
    try:
        teacher = models.Teacher.objects.get(pk=pk)
    except ObjectDoesNotExist:
        print("您想编辑的条目不存在.")
    if request.method == 'POST':
        form = forms.TeacherForm(request.POST, instance=teacher)
        if 'teacher_num' in form.changed_data:
            form.errors.clear()
            form.errors['teacher_num'] = '错误，教师工号不可修改'
            return render(request, 'school/update_teacher.html', context={'form': form})
        if form.is_valid():
            form.save()
            return redirect('teacher')
    else:
        form = forms.TeacherForm(instance=teacher)
    return render(request, 'school/update_teacher.html', context={'form': form})


def add_teacher_view(request):
    form = forms.TeacherForm()
    if request.method == 'POST':
        form = forms.TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            # return 才能跳出当前方法 实现重定向
            return HttpResponseRedirect('teacher')
    return render(request, 'school/add_teacher.html', context={'form': form})


# 建议是否改成确定删除
def delete_teacher_view(request, pk):
    try:
        teacher = models.Teacher.objects.get(pk=pk)
    except ObjectDoesNotExist:
        messages.error(request, '错误：不存在这个条目，不可删除')
    try:
        teacher.delete()
    except ProtectedError:
        messages.error(request, '错误：存在关联信息，不可删除')
    return redirect('teacher')


def student_view(request):
    form = forms.StudentForm()
    students = models.Student.objects.all()
    if request.method == 'POST':
        form = forms.StudentForm(request.POST)
        print(form.data)
        ret = {}
        for key, value in form.data.items():
            if value:
                print(key, value)
                ret[key] = value
        students = models.Student.objects.filter(**ret)
    return render(request, 'school/student.html', context={'form': form, 'students': students})


def update_student_view(request, pk):
    try:
        student = models.Student.objects.get(pk=pk)
    except ObjectDoesNotExist:
        print("您想编辑的条目不存在.")
    if request.method == 'POST':
        form = forms.StudentForm(request.POST, instance=student)
        if 'student_id' in form.changed_data:
            form.errors.clear()
            form.errors['student_id'] = '错误，学号不可修改'
            return render(request, 'school/update_student.html', context={'form': form})
        if form.is_valid():
            form.save()
            return redirect('student')
    else:
        form = forms.StudentForm(instance=student)
    return render(request, 'school/update_student.html', context={'form': form})


def add_student_view(request):
    form = forms.StudentForm()
    if request.method == 'POST':
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('student')
    return render(request, 'school/add_student.html', context={'form': form})


# 建议是否改成确定删除
def delete_student_view(request, pk):
    try:
        student = models.Student.objects.get(pk=pk)
    except ObjectDoesNotExist:
        messages.error(request, '错误：不存在这个条目，不可删除')
    try:
        student.delete()
    except ProtectedError:
        messages.error(request, '错误：存在关联信息，不可删除')
    return redirect('student')


def study_delay_event_view(request):
    form = forms.StudyDelayForm()
    studies = models.StudyDelay.objects.all()
    if request.method == 'POST':
        form = forms.StudyDelayForm(request.POST)
        ret = {}
        for key, value in form.data.items():
            if value:
                ret[key] = value
        studies = models.StudyDelay.objects.filter(**ret)
    return render(request, 'school/study-delay-event.html', context={'form': form, 'studies': studies})


def update_study_delay_event_view(request, pk):
    try:
        study = models.StudyDelay.objects.get(pk=pk)
    except ObjectDoesNotExist:
        print("您想编辑的条目不存在.")
    if request.method == 'POST':
        form = forms.StudyDelayForm(request.POST, instance=study)
        if form.is_valid():
            try:
                form.save()
            except ValidationError:
                form.errors['old_class'] = '错误:班级转换信息不可修改'
                return render(request, 'school/update_study_delay_event.html', context={'form': form})
            return redirect('study-delay-event')
    else:
        form = forms.StudyDelayForm(instance=study)
    return render(request, 'school/update_study_delay_event.html', context={'form': form})


def add_study_delay_event_view(request):
    form = forms.StudyDelayForm()
    if request.method == 'POST':
        form = forms.StudyDelayForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except ValidationError:
                form.errors['old_class'] = '错误:原班级和学生现班级不一致'
                return render(request, 'school/update_study_delay_event.html', context={'form': form})
            return HttpResponseRedirect('study-delay-event')
    return render(request, 'school/add_study_delay_event.html', context={'form': form})


# 建议是否改成确定删除
def delete_study_delay_event_view(request, pk):
    try:
        study = models.StudyDelay.objects.get(pk=pk)
    except ObjectDoesNotExist:
        messages.error(request, '错误：不存在这个条目，不可删除')
    try:
        study.delete()
    except ValidationError:
        messages.error(request, '错误：新班级和学生现班级不一致')
    return redirect('study-delay-event')


def change_major_event_view(request):
    form = forms.ChangeMajorForm()
    studies = models.ChangeMajor.objects.all()
    if request.method == 'POST':
        form = forms.ChangeMajorForm(request.POST)
        ret = {}
        for key, value in form.data.items():
            if value:
                ret[key] = value
        studies = models.ChangeMajor.objects.filter(**ret)
    return render(request, 'school/change-major-event.html', context={'form': form, 'studies': studies})


def update_change_major_event_view(request, pk):
    try:
        study = models.ChangeMajor.objects.get(pk=pk)
    except ObjectDoesNotExist:
        print("您想编辑的条目不存在.")
    if request.method == 'POST':
        form = forms.ChangeMajor(request.POST, instance=study)
        if form.is_valid():
            try:
                form.save()
            except ValidationError:
                form.errors['old_class'] = '错误:原班级和学生现班级不一致'
                return render(request, 'school/update_change_major_event.html', context={'form': form})
            return redirect('change-major-event')
    else:
        form = forms.ChangeMajorForm(instance=study)
    return render(request, 'school/update_change_major_event.html', context={'form': form})


def add_change_major_event_view(request):
    form = forms.ChangeMajorForm()
    if request.method == 'POST':
        form = forms.ChangeMajorForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except ValidationError:
                form.errors['old_class'] = '错误:原班级和学生现班级不一致'
                return render(request, 'school/add_change_major_event.html', context={'form': form})
            return HttpResponseRedirect('change-major-event')
    return render(request, 'school/add_change_major_event.html', context={'form': form})


# 建议是否改成确定删除
def delete_change_major_event_view(request, pk):
    try:
        study = models.ChangeMajor.objects.get(pk=pk)
    except ObjectDoesNotExist:
        messages.error(request, '错误：不存在这个条目，不可删除')
    try:
        study.delete()
    except ValidationError:
        messages.error(request, '错误：新班级和学生现班级不一致')
    return redirect('change-major-event')


def course_view(request):
    form = forms.CourseForm()
    courses = models.Course.objects.all()
    if request.method == 'POST':
        form = forms.CourseForm(request.POST)
        ret = {}
        for key, value in form.data.items():
            if value:
                ret[key] = value
        courses = models.Course.objects.filter(**ret)
    return render(request, 'school/course.html', context={'form': form, 'courses': courses})


def update_course_view(request, pk):
    try:
        course = models.Course.objects.get(pk=pk)
    except ObjectDoesNotExist:
        print("您想编辑的条目不存在.")
    if request.method == 'POST':
        form = forms.CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course')
    else:
        form = forms.CourseForm(instance=course)
    return render(request, 'school/update_course.html', context={'form': form})


def add_course_view(request):
    form = forms.CourseForm()
    if request.method == 'POST':
        form = forms.CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('course')
    return render(request, 'school/add_course.html', context={'form': form})


# 建议是否改成确定删除
def delete_course_view(request, pk):
    try:
        course = models.Course.objects.get(pk=pk)
    except ObjectDoesNotExist:
        messages.error(request, '错误：不存在这个条目，不可删除')
    try:
        course.delete()
    except ProtectedError:
        messages.error(request, '错误：存在关联信息，不可删除')
    return redirect('course')


def started_course_view(request):
    form = forms.StartedCourseInfoForm()
    courses = models.StartedCourseInfo.objects.all()
    if request.method == 'POST':
        form = forms.StartedCourseInfoForm(request.POST)
        ret = {}
        for key, value in form.data.items():
            if value:
                ret[key] = value
        courses = models.StartedCourseInfo.objects.filter(**ret)
    return render(request, 'school/started_course.html', context={'form': form, 'courses': courses})


def update_started_course_view(request, pk):
    try:
        started_course = models.StartedCourseInfo.objects.get(pk=pk)
    except ObjectDoesNotExist:
        print("您想编辑的条目不存在.")
    if request.method == 'POST':
        form = forms.StartedCourseInfoForm(request.POST, instance=started_course)
        if form.is_valid():
            form.save()
            return redirect('started-course')
    else:
        form = forms.StartedCourseInfoForm(instance=started_course)
    return render(request, 'school/update_started_course.html', context={'form': form})


def add_started_course_view(request):
    form = forms.StartedCourseInfoForm()
    if request.method == 'POST':
        form = forms.StartedCourseInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('started-course')
    return render(request, 'school/add_started_course.html', context={'form': form})


# 建议是否改成确定删除
def delete_started_course_view(request, pk):
    try:
        started_course = models.StartedCourseInfo.objects.get(pk=pk)
    except ObjectDoesNotExist:
        messages.error(request, '错误：不存在这个条目，不可删除')
    try:
        started_course.delete()
    except ProtectedError:
        messages.error(request, '错误：存在关联信息，不可删除')
    return redirect('started-course')


def select_course_view(request):
    form = forms.ChooseCourseForm()
    select_courses = models.ChooseCourse.objects.all()
    if request.method == 'POST':
        form = forms.ChooseCourseForm(request.POST)
        ret = {}
        for key, value in form.data.items():
            if value:
                ret[key] = value
        select_courses = models.ChooseCourse.objects.filter(**ret)
    return render(request, 'school/select_course.html', context={'form': form, 'courses': select_courses})


def update_select_course_view(request, pk):
    try:
        select_course = models.ChooseCourse.objects.get(pk=pk)
    except ObjectDoesNotExist:
        print("您想编辑的条目不存在.")
    if request.method == 'POST':
        form = forms.ChooseCourseForm(request.POST, instance=select_course)
        if form.is_valid():
            form.save()
            return redirect('select-course')
    else:
        form = forms.ChooseCourseForm(instance=select_course)
    return render(request, 'school/update_select_course.html', context={'form': form})


def add_select_course_view(request):
    form = forms.ChooseCourseForm()
    if request.method == 'POST':
        form = forms.ChooseCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('select-course')
    return render(request, 'school/add_select_course.html', context={'form': form})


# 建议是否改成确定删除
def delete_select_course_view(request, pk):
    try:
        select_course = models.ChooseCourse.objects.get(pk=pk)
    except ObjectDoesNotExist:
        messages.error(request, '错误：不存在这个条目，不可删除')
    try:
        select_course.delete()
    except ProtectedError:
        messages.error(request, '错误：存在关联信息，不可删除')
    return redirect('select-course')

