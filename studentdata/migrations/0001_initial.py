# Generated by Django 3.1.5 on 2021-01-18 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Studentreg2',
            fields=[
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=100)),
                ('reg_no', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Studentreg',
            },
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('subject_name', models.CharField(max_length=200)),
                ('subject_code', models.CharField(max_length=200, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Subjects',
            },
        ),
        migrations.CreateModel(
            name='LinkSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_no', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='studentdata.studentreg2')),
                ('subject_code', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='studentdata.subjects')),
            ],
            options={
                'db_table': 'LinkSubject',
            },
        ),
        migrations.CreateModel(
            name='BranchSem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=200)),
                ('reg_no', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='studentdata.studentreg2')),
            ],
            options={
                'db_table': 'BranchSem',
            },
        ),
    ]
