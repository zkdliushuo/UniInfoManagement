# Lab 3 -- Database Application Development

项目地址：https://github.com/zkdliushuo/UniInfoManagement

部署好的系统入口：http://121.89.166.136:8080/index

组员：刘硕 万琪 牛田 张鑾翔

[TOC]

![1](./1.jpeg)

## 实验概述

​	在实验二的基础上设计开发了一个高校信息管理系统。存储了校区信息、学生信息、教师信息、班级信息、学籍变动等数据，并且在这些数据的基础上，使用Django+MySQL实现了校区管理、专业管理、学生信息管理等一系列功能。我们实现了全部的前端和后端操作，目前没有引入登录用户验证等权限操作。

### 实验环境

- Django2.0.2 (SQLite3)
- Bootstrap
- Python 3.8
- 实验系统：Ubuntu 18.04

### 安装运行

```shell
$ git clone https://github.com/zkdliushuo/UniInfoManagement.git

$ cd UniInfoManagement/backend/schoolmanagement-master/

$ pip install -r requirements.txt

$ python manage.py migrate

$ python manage.py loaddata initial_data.json

$ python manage.py loaddata schoolmanagement\fixtures\initial_data.json

$ python manage.py runserver
// 推荐在虚拟环境下执行
```

### 登录界面

​	之后在访问http://127.0.0.1:8000/index 既可以登录系统，此时的界面应该是如下的：

![1590233594692](assets/1590233594692.png)

左侧的sidebar罗列出了所有的管理选项，对应于数据库中所有的table.

### 实现的功能

​	我们组实现了实验手册中的全部要求，包括：所有table的所有信息的增删查改，关联信息保护防止误删除，工号、代码、学号等部分主键信息不可删除的要求，灵活搜索功能：包括按照单个字段和多个字段搜索，教师离职导致的课程移交操作，学生毕业之前不允许删除，以及一定的出错处理，包括：学生重复修读同一课程号的课程、删除学籍异动信息可能导致的信息不一致清况等。

## 系统总体设计

### 系统模块结构

#### 项目目录结构

![](./project_structure.png)

##### school文件夹

​	我们的程序代码主要是在school文件夹下面。

​	models.py 存放的是数据库代码，包括：Campus，Major，Classes，People，Student，Teacher，StudyDelay，ChangeMajor，Course，Startedcourse，ChooseCourese。分别对应校区，专业，学生，教师，学籍异动(抽象类，不在数据库中建立相应的table)。

​	views.py是另外一个十分的文件，描述了我们处理增删查改和离职等请求操作的逻辑。

​	forms.py主要用来描述我们需要用到的表单信息，对于大部分table其表单都和本身的字段名相同。但为了支持离职操作，我们把开课课程表的表单进行了一些处理。

​	school下的其它文件和文件夹都是用来服务于Django的系统运行。

##### schoolmanagement文件夹

​	这里主要有俩个文件很重要。settings.py提供了Django的定制服务，我们在这里设置了数据库为SQLite3(Django原生支持的数据库)，设置部署服务器的相关信息和其它信息。

​	urls.py用来处理路由转发，为了简单，我们把所有路由设置为单层路由。

##### manage.py

​	用来和Django交互，执行命令行操作。

##### templates

​	存放前端网页设计。

##### static

​	存放图标等信息。

##### venv

​	虚拟环境依赖。

### 工作流程

​	按照从总体到局部的方式描述工作流程。

​	适用GET方法请求index后，该Http请求发送到urls.py(Django的路由器)，之后根据路由表的设置，将该访问转发给views的home_view方法。在这里，我们返回一个空表单给前端。于是可以看到这张图：

![1590233594692](assets/1590233594692.png)

​	点击左侧任一按钮，即可跳转到对应界面。以点击教师管理为例(为了说明教师离职功能)，点击其它按钮的工作流程类似。点击之后，进入teacher-view。

​	![1590238401366](assets/1590238401366.png)

​	在这里，和其它每个界面一样，我们设计了四种操作：

​	查询：	在上侧的表单中填入任意的查询信息组合，然后点击查询就可以在这个界面(teacher-view)下显示所有查询结果。关于查询等操作的结果，后面会有详细的介绍。

​	添加记录：	点击添加记录按钮，系统会跳转到添加一个教师的界面，即add-teacher-view，如下：

![1590238764658](assets/1590238764658.png)

​	填写对应的信息点击提交就可以尝试提交这个增操作到数据库，如果不符合增操作的条件，会在当前界面add-teacher-view的对应的字段产生报错信息。如果点击取消，就可以返回到前面的界面，即teacher-view.

​	修改操作：	点击在对应教师的每一行的右侧的绿色按钮即可跳转到修改操作的界面，即update-teacher-view，如下：

![1590239045256](assets/1590239045256.png)

​	更新操作和增加操作类似。在对应的字段会有对应的报错信息的提示。如修改教师的教职工编号就会有报错。

​	移除操作：	点击对应教师右侧的红色按钮可以进行教师的离职操作，相应的页面跳转到leave-teacher-view视图，如下：

![1590242146785](assets/1590242146785.png)

​	可以看到这里列出了所有该教师带的课程（上方的一些文字是前端的小bug，没来的及修改，请忽略），只有开课教师一栏是可修改的，其它栏只是用来提示是哪门课需要移交。选择好教师后，点击右侧移交。系统在当前页面重新显示剩下的这个教师代理的课程，如下：

![1590242294730](assets/1590242294730.png)

​	再次移交这个教师就会被删除(离职完成)，如下：

![1590242331361](assets/1590242331361.png)

​	其它的操作于此类似。

### 数据库设计

​	数据库的设计和实验手册的有一些微小的出入，主要在日期的设置上。下面分别介绍各个表的设计：

#### Campus 校区

![1590242524265](assets/1590242524265.png)

​	campus平平无奇，没有外键等。

#### Major 专业

![1590242584723](assets/1590242584723.png)

​	外键是campus。设置了级联删除的保护。设置代码如下：

```python
campus = models.ForeignKey(Campus, verbose_name='校区', on_delete=models.PROTECT)
```

​	on_delete=models.PROTECT 表示如果在删除campus的元组的时候，如果存在对这个元组的外键引用，就不能删除，并且触发一个ProtectedError错误信息。我们通过处理这个信息，在前端可以显示相应的报错。

​	后面的保护级联删除的操作是类似的，我就不再列出相关代码。

#### Classes 班级

​	![1590242788079](assets/1590242788079.png)

​	班级部分设置了外键专业，同样有级联删除的保护设置。班级的所在年级属性(grade)被我设置为了一个选择集合，可以在1984年到2020年之间任意选择(如果以后有机会，把这里可以用更好的动态办法设置为自动更新到今年，现在的2020是我手动设置的)。

#### People 教师和学生的父表

​	People表是数据库的抽象基类，是Teacher和student的抽象父类。其在数据库中没有相对于的实例化表，因此无法列出其数据库中的实例。

​	people的对应在Django的ORM操作序列如下：

```python
class People(models.Model):
    def idvalidator(self):
        if len(self) != 18:
            raise ValueError('请输入18位身份证号码,您只输入了%s位' % len(self))

    identification = models.CharField('身份信息号', primary_key=True, max_length=18, unique=True, validators=[idvalidator])
    ID_CARD = '身份证'
    PASSPORT = '护照'
    ID_TYPE_CHOICES = (
        (ID_CARD, '身份证'),
        (PASSPORT, '护照'),
    )
    id_type = models.CharField('身份信息类型', max_length=7, choices=ID_TYPE_CHOICES, default=ID_CARD)
    chinese_name = models.CharField('中文名', max_length=10, null=False)
    MALE = '男'
    FEMALE = '女'
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
```

​	People集合了Teacher和Student实体的共同属性，**并且给身份证号和护照号均设置了验证器（验证编号长度必须为18位**，我也不知道护照号是多少位qwq，为了简洁，这里统一设置为了18位，可以很简单地改成对身份证和护照号分别验证）。just for real!

​	People没有外键，外键都加在了其子类上。下面介绍其子类。

#### Teacher 教师

​	教师的table比较大，不好截屏，这里把他的DDL定义列出来：

```sql
create table school_teacher
(
    identification   varchar(18)  not null
        primary key,
    id_type          varchar(7)   not null,
    chinese_name     varchar(10)  not null,
    gender_type      varchar(3)   not null,
    birth_date       date         not null,
    nationality      varchar(20)  not null,
    family_addr      varchar(200),
    family_post_code varchar(6),
    family_phone_num varchar(11),
    teacher_num      varchar(10)  not null
        unique,
    join_date        date         not null,
    email            varchar(254) not null,
    rank             varchar(7)   not null,
    major_id         varchar(3)   not null
        references school_major
            deferrable initially deferred
);

create index school_teacher_major_id_9ae82cf0
    on school_teacher (major_id);
```

​	其身份证件号identification为主键，教职工号teacher_num要求唯一unique，所在专业是外键引用Major类（school_major）。

#### Student 学生

​	和教师及其类似。只是把教职工号改成学号，外键的专业改成班级。DDL语言定义如下：

```sqlite
create table school_student
(
    identification   varchar(18)  not null
        primary key,
    id_type          varchar(7)   not null,
    chinese_name     varchar(10)  not null,
    gender_type      varchar(3)   not null,
    birth_date       date         not null,
    nationality      varchar(20)  not null,
    family_addr      varchar(200),
    family_post_code varchar(6),
    family_phone_num varchar(11),
    student_id       varchar(10)  not null
        unique,
    start_date       date         not null,
    email            varchar(254) not null,
    classes_id       varchar(9)   not null
        references school_classes
            deferrable initially deferred
);

create index school_student_classes_id_02b2ecbf
    on school_student (classes_id);
```

#### StudyEvent 学籍异动

​	是StudyDelay和ChangeMajor表的抽象基类。不详细描述。

#### StudyDelay 降级

![1590243547863](assets/1590243547863.png)

​	该表有主键event_num异动编号作为主键，俩个外键引用在classes班级表上，另外有一个外键引用在student表上。注意这里没有对任何一个外键设置级联删除保护，相反地我们设置了级联删除的一致性检查工作，这个工作通过适用Django的signal机制实现的触发器完成，**这个是实验手册上并没有要求，但是我们觉得必要的**。

​	这个触发器可以同时作用在studydelay和changemajor类上，其代码如下：

```
# 删除异动的触发器
@receiver(pre_delete, sender=ChangeMajor)
@receiver(pre_delete, sender=StudyDelay)
def post_delete_study_event(sender, instance, **kwargs):
    if instance.student.classes.id == instance.new_class.id:
        instance.student.classes = instance.old_class
        instance.student.save()
    else:
        raise ValidationError(
            message='该生记录不可删除',
            code='unique_together',
        )


@receiver(pre_save, sender=ChangeMajor)
@receiver(pre_save, sender=StudyDelay)
def post_save_study_event(sender, instance, **kwargs):
    if instance.student.classes.id == instance.old_class.id:
        instance.student.classes = instance.new_class
        instance.student.save()
    else:
        raise ValidationError(
            message='转出班级与学生班级不匹配',
            code='unique_together',
        )
```

​	这个触发器的工作大概就是验证如果删除了，是不是会产生孤立的另外一条异动信息。

#### ChangeMajor 转专业

​	和StudyDelay类似

#### Course 课程

![1590244519984](assets/1590244519984.png)

​	课程有主键作为课程号，还有课程名，以及外键引用开课的专业，还有考试方式。P表示当堂答辩，E表示考试。

#### StartedCourse 开课

![1590244617348](assets/1590244617348.png)

​	开课的这里设置了开课的编号(是默认的id)，以及外键是课程和教师，事实上这个表尽管有主键，其实是课程表和教师表的一个多对多关系。

#### ChooseCourse 选课

![1590244728559](assets/1590244728559.png)

​	选课表引用了俩个外键，一个是开课的课程号，一个是选课的学生号（学生的身份信息）。

​	保存了成绩信息，设置约束为小于等于100.







该部分伪代码如下：

```python
// 校区
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
    campus = models.ForeignKey(Campus, verbose_name='校区', on_delete=models.PROTECT)

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
    YEAR_CHOICES = [(r, r) for r in range(date.today().year + 1, 1984, -1)]
    grade = models.IntegerField(choices=YEAR_CHOICES, default=date.today().year, verbose_name='年级', null=True, blank=True)
    major = models.ForeignKey(Major, on_delete=models.PROTECT, verbose_name='专业')

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
    ID_CARD = '身份证'
    PASSPORT = '护照'
    ID_TYPE_CHOICES = (
        (ID_CARD, '身份证'),
        (PASSPORT, '护照'),
    )
    id_type = models.CharField('身份信息类型', max_length=7, choices=ID_TYPE_CHOICES, default=ID_CARD)
    chinese_name = models.CharField('中文名', max_length=10, null=False)
    MALE = '男'
    FEMALE = '女'
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
    major = models.ForeignKey(Major, on_delete=models.PROTECT, verbose_name='专业')
    ASSOCIATE_PROF = '副教授'
    PROF = '教授'
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
    classes = models.ForeignKey(Classes, on_delete=models.PROTECT, verbose_name='班级')

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
    old_class = models.ForeignKey(Classes, on_delete=models.PROTECT, verbose_name='原班级')
    new_class = models.ForeignKey(Classes, on_delete=models.PROTECT, verbose_name='新班级')

    class Meta:
        abstract = True
        # unique_together = ('old_class', 'new_class')


class ChangeMajor(StudyEvent):
    CHANGE_YES = '是'
    CHANGE_NO = '否'
    CHANGE_NOT_MEMBER = '不是团员'
    CHANGE_TYPE = (
        (CHANGE_YES, '是'),
        (CHANGE_NO, '否'),
        (CHANGE_NOT_MEMBER, '不是团员'),
    )
    change_association = models.CharField('是否转出团员关系', max_length=9, choices=CHANGE_TYPE)
    old_class = models.ForeignKey(Classes, on_delete=models.PROTECT, related_name='Change_from', verbose_name='原班级')
    new_class = models.ForeignKey(Classes, on_delete=models.PROTECT, related_name='Change_to', verbose_name='新班级')
    student = models.OneToOneField(Student, on_delete=models.PROTECT, verbose_name='异动学生')

    def __str__(self):
        return self.event_num + " 转专业"

    class Meta:
        verbose_name = '转专业'
        verbose_name_plural = "转专业"


class StudyDelay(StudyEvent):
    DROP = '休学'
    VOLUNTEER = '支教'
    DELAY_REASON = (
        (DROP, '休学'),
        (VOLUNTEER, '支教'),
    )
    delay_reason = models.CharField('降级原因', max_length=5, choices=DELAY_REASON)
    old_class = models.ForeignKey(Classes, on_delete=models.PROTECT, related_name='Delay_from', verbose_name='原班级')
    new_class = models.ForeignKey(Classes, on_delete=models.PROTECT, related_name='Delay_to', verbose_name='新班级')
    student = models.OneToOneField(Student, on_delete=models.PROTECT, verbose_name='异动学生')

    def __str__(self):
        return self.event_num + " 降级"

    class Meta:
        verbose_name = '降级'
        verbose_name_plural = "降级"


class Course(models.Model):
    id = models.CharField('课程号', primary_key=True, max_length=18, unique=True)
    name = models.CharField('课程名称', unique=True, max_length=100)
    school = models.ForeignKey(Major, on_delete=models.PROTECT, verbose_name='专业')
    EXAMS = '考试'
    PRESENTATION = '当堂答辩'
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
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT, verbose_name='开课教师')
    course = models.ForeignKey(Course, on_delete=models.PROTECT, verbose_name='开课课程')
    YEAR_CHOICES = [(r, r) for r in range(date.today().year + 1, 1984, -1)]
    year_start = models.IntegerField(choices=YEAR_CHOICES, default=date.today().year, verbose_name='开课年份', null=True, blank=True)
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
        return self.course.name+" "+self.teacher.chinese_name+" "+str(self.year_start)+" "+self.semester_start

    class Meta:
        verbose_name = '开课'
        verbose_name_plural = "开课"


class ChooseCourse(models.Model):
    course = models.ForeignKey(StartedCourseInfo, on_delete=models.PROTECT, verbose_name='选课课程')
    student = models.ForeignKey(Student, on_delete=models.PROTECT, verbose_name='选课学生')
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
    if instance.student.classes.id == instance.new_class.id:
        instance.student.classes = instance.old_class
        instance.student.save()
    else:
        raise ValidationError(
            message='该生记录不可删除',
            code='unique_together',
        )


@receiver(pre_save, sender=ChangeMajor)
@receiver(pre_save, sender=StudyDelay)
def post_save_study_event(sender, instance, **kwargs):
    if instance.student.classes.id == instance.old_class.id:
        instance.student.classes = instance.new_class
        instance.student.save()
    else:
        raise ValidationError(
            message='转出班级与学生班级不匹配',
            code='unique_together',
        )


```

## 系统详细设计

### 路由模块

#### 模块的输入

​	路由模块的代码如下：

```python
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
    # path('leave-teacher/<pk>', views.teacher_view, name='teacher'),
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
    path('update-started-course/<int:pk>', views.update_started_course_view, name='update-started-course'),
    path('add-started-course', views.add_started_course_view, name='add-started-course'),
    path('delete-started-course/<int:pk>', views.delete_started_course_view, name='delete-started-course'),

    path('select-course', views.select_course_view, name='select-course'),
    path('update-select-course/<int:pk>', views.update_select_course_view, name='update-select-course'),
    path('add-select-course', views.add_select_course_view, name='add-select-course'),
    path('delete-select-course/<int:pk>', views.delete_select_course_view, name='delete-select-course'),
```

​	其接受浏览器发来的url请求，处理根url下的其它字段，解析其中的参数字段，如上面的<int:pk>，分别得到对应的路由路径。

​	路由模块还接受来自views的输入，用来在视图函数中，通过选择重定向的路径，直接返回相应的页面进行渲染。

#### 模块的输出

​	输出的值主要是作为views中的函数的参数传入，主要包括：

request：Django支持的Http报头格式，包括了报头信息，验证的Token等。

参数：一般在update和delete的时候在url后面附着一个字段表示需要操作的

## 系统实现与测试

### 专业管理功能

1. 运行界面

   ![](./major_management.png)

2. 实现

   （TBD）

3. 测试结果

   （TBD）

### 学生管理功能

（TBD）

### 教师管理功能

（TBD）

### 班级管理功能

（TBD）

### 校区管理功能

（TBD）

### 学籍异动管理功能

（TBD）

### 课程管理功能

（TBD）

### 教师开课管理功能

（TBD）

### 学生选课管理功能

（TBD）

### 搜索功能

（TBD）

## 总结与讨论

（TBD）

## 分工情况

（TBD）

