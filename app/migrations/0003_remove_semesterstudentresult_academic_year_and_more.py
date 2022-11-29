# Generated by Django 4.1.3 on 2022-11-29 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_overallresult_ca_remove_overallresult_fe_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='semesterstudentresult',
            name='academic_year',
        ),
        migrations.AddField(
            model_name='semesterstudentresult',
            name='semester',
            field=models.IntegerField(choices=[(1, 'Semester 1'), (2, 'Semester e')], default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='admission',
            field=models.CharField(max_length=200, verbose_name='Admission Number'),
        ),
    ]