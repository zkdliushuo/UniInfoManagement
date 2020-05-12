from django.db import models
from django.contrib.auth.models import User
from datetime import date
# 验证器
from django.core.exceptions import ValidationError


# Create your models here.


class TeacherExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    salary = models.PositiveIntegerField(null=False)
    joindate = models.DateField(auto_now_add=True)
    mobile = models.CharField(max_length=40)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name

    @property
    def get_id(self):
        return self.user.id

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name


classes = [('one', 'one'), ('two', 'two'), ('three', 'three'), ('four', 'four'), ('five', 'five'), ('six', 'six'),
           ('seven', 'seven'), ('eight', 'eight'), ('nine', 'nine'), ('ten', 'ten')]


class StudentExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll = models.CharField(max_length=10)
    mobile = models.CharField(max_length=40, null=True)
    fee = models.PositiveIntegerField(null=True)
    cl = models.CharField(max_length=10, choices=classes, default='one')
    status = models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return self.user.first_name


class Attendance(models.Model):
    roll = models.CharField(max_length=10, null=True)
    date = models.DateField()
    cl = models.CharField(max_length=10)
    present_status = models.CharField(max_length=10)


class Notice(models.Model):
    date = models.DateField(auto_now=True)
    by = models.CharField(max_length=20, null=True, default='school')
    message = models.CharField(max_length=500)


class Campus(models.Model):
    name = models.CharField(max_length=20, null=False, unique=True)
    address = models.CharField(max_length=200, null=False, unique=True)


class Major(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)
    address = models.CharField(max_length=100, null=False)
    charger = models.CharField(max_length=50, null=False)
    campus = models.ForeignKey(Campus, on_delete=models.PROTECT)


class Classes(models.Model):
    name = models.CharField(max_length=50, unique=True)
    start_date = models.DateField(auto_now_add=True)
    head_teacher = models.CharField(max_length=50)
    grade = models.IntegerField(max_length=4)
    major = models.ForeignKey(Major, on_delete=models.PROTECT)


class People(models.Model):
    def idvalidator(self, value):
        if len(value) != 18:
            raise ValueError('请输入18位身份证号码,您只输入了%s位' % len(value))

    identification = models.CharField(primary_key=True, max_length=18, unique=True, validators=[idvalidator])
    ID_CARD = 'ID'
    PASSPORT = 'PA'
    ID_TYPE_CHOICES = (
        (ID_CARD, '身份证'),
        (PASSPORT, '护照'),
    )
    id_type = models.CharField(max_length=7, choices=ID_TYPE_CHOICES, default=ID_CARD)
    chinese_name = models.CharField(max_length=10, null=False)
    MALE = 'M'
    FEMALE = 'F'
    GENDER_TYPE_CHOICES = (
        (MALE, '男'),
        (FEMALE, '女'),
    )
    gender_type = models.CharField(max_length=3, choices=GENDER_TYPE_CHOICES)
    birth_date = models.DateField()
    nationality = models.CharField(max_length=20)
    family_addr = models.CharField(max_length=200, null=False)
    family_post_code = models.CharField(max_length=6, null=False)
    family_phone_num = models.IntegerField(max_length=11, null=False)

    # 抽象类，用来继承，可以再考虑是不是抽象(是否需要多表)
    class Meta:
        abstract = True


class Teacher(People):
    teacher_num = models.CharField(max_length=10, unique=True)
    join_date = models.DateField()
    email = models.EmailField()
    major = models.ForeignKey(Major, on_delete=models.PROTECT)
    ASSOCIATE_PROF = 'AP'
    PROF = 'P'
    RANK_TYPE_CHOICES = (
        (ASSOCIATE_PROF, '副教授'),
        (PROF, '教授')
    )
    rank = models.CharField(max_length=7, choices=RANK_TYPE_CHOICES)


class Student(People):
    student_id = models.CharField(max_length=10, unique=True)
    start_date = models.DateField()
    email = models.EmailField()
    classes = models.ForeignKey(Classes, on_delete=models.PROTECT)


class StudyEvent(models.Model):
    class Meta:
        abstract = True

    event_num = models.CharField(max_length=10, primary_key=True)
    date = models.DateField()
    old_class = models.ForeignKey(Classes, on_delete=False)
    new_class = models.ForeignKey(Classes, on_delete=False)




