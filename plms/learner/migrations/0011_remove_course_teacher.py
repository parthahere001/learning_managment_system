# Generated by Django 4.0.6 on 2022-07-18 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learner', '0010_alter_course_cresource'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='teacher',
        ),
    ]