# Generated by Django 3.2.18 on 2023-11-18 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_jobuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('JobTitle', models.CharField(max_length=50)),
                ('Description', models.CharField(max_length=300)),
                ('location', models.CharField(max_length=50)),
                ('salary_package', models.CharField(max_length=50)),
                ('PostDate', models.DateField()),
            ],
        ),
    ]
