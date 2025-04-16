# Generated by Django 5.1.7 on 2025-04-15 21:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField(max_length=150)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('year_of_release', models.IntegerField(max_length=4)),
                ('mileage', models.TextField(max_length=15)),
                ('PTC', models.TextField(max_length=20)),
                ('owner', models.IntegerField(max_length=1)),
                ('сondition', models.TextField(max_length=10)),
                ('power', models.TextField(max_length=10)),
                ('engine_capacity', models.TextField(max_length=10)),
                ('engine_type', models.TextField(max_length=10)),
                ('transmission_box', models.TextField(max_length=20)),
                ('drive', models.TextField(max_length=20)),
                ('Equipment', models.TextField(max_length=20)),
                ('Body_type', models.TextField(max_length=10)),
                ('colour', models.TextField(max_length=10)),
                ('wheel', models.TextField(max_length=10)),
                ('url_for_vidio', models.URLField()),
                ('history', models.TextField(blank=True, default='', max_length=2000, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
            ],
            options={
                'verbose_name': 'Car',
                'verbose_name_plural': 'Cars',
            },
        ),
    ]
