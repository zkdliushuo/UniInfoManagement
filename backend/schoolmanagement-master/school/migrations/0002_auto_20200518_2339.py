# Generated by Django 3.0.5 on 2020-05-18 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='changemajor',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='school.Student'),
        ),
        migrations.AlterField(
            model_name='studydelay',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='school.Student'),
        ),
    ]
