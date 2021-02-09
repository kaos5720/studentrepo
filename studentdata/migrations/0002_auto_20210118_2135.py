# Generated by Django 3.1.5 on 2021-01-18 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentdata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('branch_name', models.CharField(max_length=200)),
                ('branch_code', models.CharField(max_length=200, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Branch',
            },
        ),
        migrations.CreateModel(
            name='Sem',
            fields=[
                ('sem_id', models.AutoField(primary_key=True, serialize=False)),
                ('branch_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentdata.branch')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_marks', models.IntegerField(max_length=10)),
                ('reg_no', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='studentdata.studentreg2')),
                ('sem_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='studentdata.sem')),
                ('subject_code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='studentdata.subjects')),
            ],
        ),
        migrations.RemoveField(
            model_name='linksubject',
            name='reg_no',
        ),
        migrations.RemoveField(
            model_name='linksubject',
            name='subject_code',
        ),
        migrations.DeleteModel(
            name='BranchSem',
        ),
        migrations.DeleteModel(
            name='LinkSubject',
        ),
        migrations.AddField(
            model_name='studentreg2',
            name='branch_code',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='studentdata.branch'),
        ),
        migrations.AddField(
            model_name='studentreg2',
            name='sem',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='studentdata.sem'),
        ),
        migrations.AddField(
            model_name='subjects',
            name='sem_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='studentdata.sem'),
        ),
    ]
