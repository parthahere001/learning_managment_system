# Generated by Django 4.0.6 on 2022-07-15 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learner', '0002_course_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='fek',
            field=models.CharField(default=3, max_length=50),
            preserve_default=False,
        ),
    ]