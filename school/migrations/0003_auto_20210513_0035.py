# Generated by Django 3.2 on 2021-05-12 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20210512_0507'),
    ]

    operations = [
        migrations.AddField(
            model_name='months',
            name='student',
            field=models.ForeignKey(default=28, on_delete=django.db.models.deletion.CASCADE, to='school.studentsdetail'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentsdetail',
            name='address',
            field=models.CharField(default=29, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentsdetail',
            name='fm_number',
            field=models.CharField(default=28, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentsdetail',
            name='sex',
            field=models.BooleanField(default=True),
        ),
    ]