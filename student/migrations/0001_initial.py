# Generated by Django 2.1 on 2019-11-06 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.TextField()),
                ('name', models.TextField(max_length=40)),
                ('stud_class', models.TextField()),
                ('department', models.TextField()),
            ],
        ),
    ]