# Generated by Django 3.2 on 2021-05-29 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0011_marks_schoolclasses_subjects'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentsdetail',
            name='id',
        ),
        migrations.AddField(
            model_name='studentsdetail',
            name='rollnbr',
            field=models.BigAutoField(primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
