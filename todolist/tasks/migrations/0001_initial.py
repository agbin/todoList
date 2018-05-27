# Generated by Django 2.0.5 on 2018-05-27 10:31

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Name')),
                ('color', colorfield.fields.ColorField(default='#FF0000', max_length=18)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.Category', verbose_name='Category')),
            ],
        ),
    ]
