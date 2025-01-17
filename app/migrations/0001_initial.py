# Generated by Django 4.1.3 on 2022-11-29 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Class Name')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Student Name')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Department Name')),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Module Name')),
                ('code', models.CharField(max_length=200, verbose_name='Module Code')),
                ('credits', models.IntegerField()),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.department')),
            ],
        ),
        migrations.CreateModel(
            name='NTALevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Level Name')),
                ('semester', models.CharField(max_length=200, verbose_name='Semester Name')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Student Name')),
                ('reg_no', models.CharField(max_length=200, verbose_name='Registration Number')),
                ('form_four', models.CharField(max_length=200, verbose_name='Form Four Index Number')),
                ('admission', models.CharField(max_length=200, verbose_name='Registration Number')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.course')),
            ],
        ),
        migrations.CreateModel(
            name='SemesterStudentResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academic_year', models.CharField(max_length=200, verbose_name='Academic Year')),
                ('module', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.module')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.student')),
            ],
        ),
        migrations.CreateModel(
            name='OverallResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academic_year', models.CharField(max_length=200, verbose_name='Academic Year')),
                ('credits', models.FloatField()),
                ('is_pass', models.BooleanField()),
                ('ca', models.FloatField(verbose_name='Continuous Assessments')),
                ('fe', models.FloatField(verbose_name='Final Examination')),
                ('status', models.IntegerField(choices=[(0, 'Enrollment Complete')])),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.student')),
            ],
        ),
        migrations.AddField(
            model_name='module',
            name='nta_level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.ntalevel'),
        ),
        migrations.CreateModel(
            name='HOD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='HOD Name')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.department')),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starting_year', models.DateTimeField()),
                ('enrollment_status', models.IntegerField(choices=[(0, 'Enrollment Complete')])),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.student')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.department'),
        ),
        migrations.CreateModel(
            name='ClassModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Class', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.class')),
                ('module', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.module')),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.course'),
        ),
        migrations.AddField(
            model_name='class',
            name='nta_level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.ntalevel'),
        ),
    ]
