# Generated by Django 4.1 on 2022-08-30 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0004_department_student'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Model1',
        ),
        migrations.DeleteModel(
            name='Model2',
        ),
        migrations.AddField(
            model_name='student',
            name='Age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='Dob',
            field=models.DateField(),
        ),
    ]
