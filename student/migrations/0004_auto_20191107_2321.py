# Generated by Django 2.1 on 2019-11-07 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20191107_2317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marks',
            name='student',
        ),
        migrations.AddField(
            model_name='year',
            name='sub',
            field=models.ManyToManyField(blank=True, to='student.Marks'),
        ),
    ]
