# Generated by Django 5.0.4 on 2024-06-03 18:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('phone_number', models.CharField(max_length=10)),
                ('watsapp_number', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='School.branch')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parents', to='School.school')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('roll_number', models.IntegerField()),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='School.parent')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='School.school')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('phone_number', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=1)),
                ('age', models.IntegerField()),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='School.branch')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='School.school')),
            ],
        ),
    ]