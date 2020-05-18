from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.core.exceptions import ValidationError
from django.db.models.signals import post_delete, post_save, pre_delete
from django.dispatch import receiver

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


class StudentExtra(models.Model):
    classes = [('one', 'one'), ('two', 'two'), ('three', 'three'), ('four', 'four'), ('five', 'five'), ('six', 'six'),
               ('seven', 'seven'), ('eight', 'eight'), ('nine', 'nine'), ('ten', 'ten')]
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
    id = models.CharField('校区代码', max_length=10, primary_key=True)
    name = models.CharField('校区名称', max_length=20, null=False, unique=True)
    address = models.CharField('校区地址', max_length=200, null=False, unique=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '校区'
        verbose_name_plural = "校区"


class Major(models.Model):
    id = models.CharField('专业代码', max_length=3, primary_key=True)
    name = models.CharField('专业名称', max_length=100, null=False, unique=True)
    address = models.CharField('专业地址', max_length=100, null=False)
    charger = models.CharField('负责人', max_length=50, null=False)
    campus = models.ForeignKey(Campus, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '专业'
        verbose_name_plural = "专业"


class Classes(models.Model):
    id = models.CharField('班级代码', max_length=9, primary_key=True)
    name = models.CharField('班级名', max_length=50, unique=True)
    start_date = models.DateField('创建时间', auto_now_add=True)
    head_teacher = models.CharField('班主任', max_length=50)
    grade = models.CharField('年级', max_length=4)
    major = models.ForeignKey(Major, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '班级'
        verbose_name_plural = "班级"


class People(models.Model):
    def idvalidator(self):
        if len(self) != 18:
            raise ValueError('请输入18位身份证号码,您只输入了%s位' % len(self))

    identification = models.CharField('身份信息号', primary_key=True, max_length=18, unique=True, validators=[idvalidator])
    ID_CARD = 'ID'
    PASSPORT = 'PA'
    ID_TYPE_CHOICES = (
        (ID_CARD, '身份证'),
        (PASSPORT, '护照'),
    )
    id_type = models.CharField('身份信息类型', max_length=7, choices=ID_TYPE_CHOICES, default=ID_CARD)
    chinese_name = models.CharField('中文名', max_length=10, null=False)
    MALE = 'M'
    FEMALE = 'F'
    GENDER_TYPE_CHOICES = (
        (MALE, '男'),
        (FEMALE, '女'),
    )
    gender_type = models.CharField('性别', max_length=3, choices=GENDER_TYPE_CHOICES)
    birth_date = models.DateField('生日')
    nationality = models.CharField('国籍', max_length=20)
    family_addr = models.CharField('家庭住址(可选)', max_length=200, null=True, blank=True)
    family_post_code = models.CharField('家庭邮编(可选)', max_length=6, null=True, blank=True)
    family_phone_num = models.CharField('家庭电话(可选)', max_length=11, null=True, blank=True)

    # 抽象类，用来继承，可以再考虑是不是抽象(是否需要多表)
    class Meta:
        abstract = True


class Teacher(People):
    teacher_num = models.CharField('教职工编号', max_length=10, unique=True)
    join_date = models.DateField('入职年月')
    email = models.EmailField('邮箱')
    major = models.ForeignKey(Major, on_delete=models.PROTECT)
    ASSOCIATE_PROF = 'AP'
    PROF = 'P'
    RANK_TYPE_CHOICES = (
        (ASSOCIATE_PROF, '副教授'),
        (PROF, '教授')
    )
    rank = models.CharField('职称', max_length=7, choices=RANK_TYPE_CHOICES)

    def __str__(self):
        return self.chinese_name

    class Meta:
        verbose_name = '教师'
        verbose_name_plural = "教师"


class Student(People):
    student_id = models.CharField('学号', max_length=10, unique=True)
    start_date = models.DateField('入学年月')
    email = models.EmailField('邮箱')
    classes = models.ForeignKey(Classes, on_delete=models.PROTECT)

    def __str__(self):
        return self.chinese_name

    class Meta:
        verbose_name = '学生'
        verbose_name_plural = "学生"


class StudyEvent(models.Model):
    class Meta:
        abstract = True

    event_num = models.CharField('异动编号', max_length=10, primary_key=True)
    date = models.DateField('异动日期')
    old_class = models.ForeignKey(Classes, on_delete=models.PROTECT)
    new_class = models.ForeignKey(Classes, on_delete=models.PROTECT)

    class Meta:
        abstract = True
        # unique_together = ('old_class', 'new_class')


class ChangeMajor(StudyEvent):
    CHANGE_YES = 'Y'
    CHANGE_NO = 'N'
    CHANGE_NOT_MEMBER = 'NM'
    CHANGE_TYPE = (
        (CHANGE_YES, '是'),
        (CHANGE_NO, '否'),
        (CHANGE_NOT_MEMBER, '不是团员'),
    )
    change_association = models.CharField('是否转出团员关系', max_length=9, choices=CHANGE_TYPE)
    old_class = models.ForeignKey(Classes, on_delete=models.PROTECT, related_name='Change_from')
    new_class = models.ForeignKey(Classes, on_delete=models.PROTECT, related_name='Change_to')
    student = models.OneToOneField(Student, on_delete=models.PROTECT)

    def __str__(self):
        return self.event_num + " 转专业"

    class Meta:
        verbose_name = '转专业'
        verbose_name_plural = "转专业"


class StudyDelay(StudyEvent):
    DROP = 'D'
    VOLUNTEER = 'V'
    DELAY_REASON = (
        (DROP, '休学'),
        (VOLUNTEER, '支教'),
    )
    delay_reason = models.CharField('降级原因', max_length=5, choices=DELAY_REASON)
    old_class = models.ForeignKey(Classes, on_delete=models.PROTECT, related_name='Delay_from')
    new_class = models.ForeignKey(Classes, on_delete=models.PROTECT, related_name='Delay_to')
    student = models.OneToOneField(Student, on_delete=models.PROTECT)

    def __str__(self):
        return self.event_num + " 降级"

    class Meta:
        verbose_name = '降级'
        verbose_name_plural = "降级"


class Course(models.Model):
    id = models.CharField('课程号', primary_key=True, max_length=18, unique=True)
    name = models.CharField('课程名称', unique=True, max_length=100)
    school = models.ForeignKey(Major, on_delete=models.PROTECT)
    EXAMS = 'E'
    PRESENTATION = 'P'
    TEST_TYPE = (
        (EXAMS, '考试'),
        (PRESENTATION, '当堂答辩'),
    )
    grade_info = models.CharField('考试方式', max_length=9, choices=TEST_TYPE)
    teachers = models.ManyToManyField(
        Teacher,
        through='StartedCourseInfo',
        through_fields=('course', 'teacher'),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = "课程"


class StartedCourseInfo(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    year_start = models.DateField('开课年份')
    SPRING = '春季'
    AUTUMN = '秋季'
    SUMMER = '夏季'
    SEMESTER = (
        (SPRING, '春季'),
        (SUMMER, '夏季'),
        (AUTUMN, '秋季'),
    )
    semester_start = models.CharField('开课学期', max_length=7, choices=SEMESTER)
    DAY = (
        ('Mon', '周一'),
        ('Tus', '周二'),
        ('Wen', '周三'),
        ('Thu', '周四'),
        ('Fri', '周五'),
    )
    day_start = models.CharField('上课日期', max_length=5, choices=DAY)
    WHEN = (
        ('1', '第一节'),
        ('2', '第二节'),
        ('3', '第三节'),
        ('4', '第四节'),
        ('5', '第五节'),
        ('6', '第六节'),
        ('7', '第七节'),
        ('8', '第八节'),
        ('9', '第九节'),
    )
    when_start = models.CharField('上课时间', max_length=7, choices=WHEN)

    def __str__(self):
        return self.course.name+" "+self.teacher.chinese_name+" "+str(self.year_start.year)+" "+self.semester_start

    class Meta:
        verbose_name = '开课'
        verbose_name_plural = "开课"


class ChooseCourse(models.Model):
    course = models.ForeignKey(StartedCourseInfo, on_delete=models.PROTECT)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    grade = models.PositiveSmallIntegerField('考试成绩', null=True)

    def __str__(self):
        return self.course.course.name + " " + self.student.student_id

    def clean(self):
        if self.__class__.objects.\
                filter(student__student_id=self.student.student_id, course__course__id=self.course.course_id).\
                exists():
            raise ValidationError(
                message='您已经选过这门课，不可以重复选课.',
                code='unique_together',
            )

    class Meta:
        verbose_name = '选课'
        verbose_name_plural = "选课"


# 删除异动的触发器
@receiver(pre_delete, sender=ChangeMajor)
@receiver(pre_delete, sender=StudyDelay)
def post_delete_study_event(sender, instance, **kwargs):
    print("=================")
    if instance.student.classes.id == instance.new_class.id:
        instance.student.classes = instance.old_class
        instance.student.save()
    else:
        raise ValidationError(
            message='该生记录不可删除',
            code='unique_together',
        )


@receiver(post_save, sender=ChangeMajor)
@receiver(post_save, sender=StudyDelay)
def post_save_study_event(sender, instance, **kwargs):
    print("=================")
    if instance.student.classes.id == instance.old_class.id:
        instance.student.classes = instance.new_class
        instance.student.save()
    else:
        raise ValidationError(
            message='转出班级与学生班级不匹配',
            code='unique_together',
        )
