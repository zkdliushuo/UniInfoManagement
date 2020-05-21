# Lab 3 -- Database Application Development

![1](./1.jpeg)

## 实验概述

在实验二的基础上设计开发了一个高校信息管理系统。存储了校区信息、学生信息、教师信息、班级信息、学籍变动等数据，并且在这些数据的基础上，使用Django+MySQL实现了校区管理、专业管理、学生信息管理等一系列功能。

## 实验环境

- Django
- MySQL

- Bootstrap
- Python

## 安装运行

```shell
$ git clone https://github.com/zkdliushuo/UniInfoManagement.git

$ cd UniInfoManagement/backend/schoolmanagement-master/

$ pip install -r requirements.txt

$ python manage.py migrate

$ python manage.py loaddata initial_data.json

$ python manage.py loaddata schoolmanagement\fixtures\initial_data.json

$ python manage.py runserver
```

之后在`http://127.0.0.1:8000/admin`下登录，用户名和密码都是`admin`。

## 系统总体设计

### 系统模块结构

#### 项目目录结构

![](./project_structure.png)

### 工作流程

（TBD）

### 数据库设计

（TBD）

## 系统详细设计

（TBD）

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

