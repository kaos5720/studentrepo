# Generated by Django 3.1.5 on 2021-01-20 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentdata', '0005_auto_20210118_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='total_marks',
            field=models.IntegerField(max_length=10, null=True),
        ),
    ]
