# Generated by Django 2.1 on 2019-11-14 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_auto_20191110_0307'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marksheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='year',
            name='sub',
        ),
        migrations.RemoveField(
            model_name='student',
            name='year',
        ),
        migrations.DeleteModel(
            name='Year',
        ),
        migrations.AddField(
            model_name='marksheet',
            name='student',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='student.Student'),
        ),
        migrations.AddField(
            model_name='marksheet',
            name='sub',
            field=models.ManyToManyField(blank=True, to='student.Marks'),
        ),
    ]
