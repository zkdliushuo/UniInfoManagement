# Generated by Django 3.0.5 on 2020-05-22 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_auto_20200520_1555'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Attendance',
        ),
        migrations.DeleteModel(
            name='Notice',
        ),
        migrations.RemoveField(
            model_name='teacherextra',
            name='user',
        ),
        migrations.DeleteModel(
            name='StudentExtra',
        ),
        migrations.DeleteModel(
            name='TeacherExtra',
        ),
    ]