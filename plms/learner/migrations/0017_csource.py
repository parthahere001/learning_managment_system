# Generated by Django 4.0.6 on 2022-07-19 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learner', '0016_student_isteacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Csource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to='')),
                ('fname', models.CharField(default='', max_length=500)),
                ('fid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learner.course')),
            ],
        ),
    ]
