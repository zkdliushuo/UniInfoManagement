在后端(本目录下)执行以下以下命令以安装依赖和初始化数据，建议创建虚拟环境并在激活虚拟环境再执行下述命令

```
pip install -r requirements.txt  
python manage.py migrate
python manage.py loaddata initial_data.json
python manage.py loaddata schoolmanagement\fixtures\initial_data.json
python manage.py runserver
```

在http://127.0.0.1:8000/admin/ 下登录

admin 

admin

可以进入数据库后端，请任意尝试，以发现数据库中还有的数据不一致的bug。



已实现的功能：

具有一定的出错处理功能

​	通过触发器实现了：学籍异动时触发更新学生班级信息

​	通过验证器实现了：增加或删除学籍异动信息时，如果原班级和转出班级不一致或现班级和新班级不一致，抛出异常；学生选择相同的课程时，抛出阻止信息

​	通过(联合)主键实现了：学籍异动中的俩种情况最多发生一次；有关联信息无法删除



\\\\ TODO

后端还需要实现views

可以考虑在后端用django自带界面实现查询功能

教师离职

学生毕业

年级和入学时间的一致性(考虑学籍异动问题)



下面放一些展示：



![1589818285154](assets/1589818285154.png)

转专业

![1589818320449](assets/1589818320449.png)

删除这个转专业信息

![1589818354001](assets/1589818354001.png)

抛出异常

![1589818378957](assets/1589818378957.png)

异常原因：该生记录不可删除

原因如下：

我后来又进行了一次降级操作，导致我现在在计科二班

![1589818419972](assets/1589818419972.png)

