# Generated by Django 3.1.5 on 2021-01-22 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentdata', '0006_auto_20210120_2154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='subject_code',
        ),
        migrations.AddField(
            model_name='student',
            name='subject_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]