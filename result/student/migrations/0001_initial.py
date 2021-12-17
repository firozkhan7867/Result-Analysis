# Generated by Django 3.1.1 on 2021-12-17 13:24

from django.db import migrations, models
import django.db.models.deletion
import student.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branches', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Branches',
            },
        ),
        migrations.CreateModel(
            name='Regulation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regulation', models.CharField(max_length=50, unique=True)),
                ('year', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('no_of_subject', models.IntegerField()),
                ('year', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(blank=True, upload_to=student.models.path_and_rename, verbose_name='Excel FIle')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.branch')),
                ('regulation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.regulation')),
            ],
            options={
                'verbose_name_plural': 'Semesters',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.CharField(max_length=15, unique=True)),
                ('name', models.CharField(blank=True, max_length=120)),
                ('section', models.IntegerField(blank=True, default=10)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.branch')),
                ('regulation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.regulation')),
                ('sem', models.ManyToManyField(to='student.Semester')),
            ],
            options={
                'verbose_name_plural': 'Students',
            },
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('code', models.CharField(max_length=20, unique=True)),
                ('marks_scored', models.IntegerField()),
                ('total_credit', models.IntegerField()),
                ('credit_scored', models.IntegerField()),
                ('pass_or_fail', models.BooleanField(default=True)),
                ('attendace', models.CharField(blank=True, max_length=5)),
                ('cgpa', models.CharField(blank=True, max_length=5)),
                ('credit_points', models.FloatField()),
                ('fail', models.BooleanField(default=False)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.branch')),
                ('regulation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.regulation')),
                ('roll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
                ('sem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.semester')),
            ],
            options={
                'verbose_name_plural': 'Subjects',
            },
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registered', models.IntegerField(blank=True)),
                ('no_of_pass', models.IntegerField(blank=True)),
                ('TCR', models.FloatField(blank=True)),
                ('TCP', models.FloatField(blank=True)),
                ('SCGPA', models.FloatField(blank=True)),
                ('roll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
                ('sem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.semester')),
                ('subject', models.ManyToManyField(to='student.Subjects')),
            ],
        ),
    ]
