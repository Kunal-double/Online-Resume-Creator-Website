# Generated by Django 4.1.1 on 2022-10-05 08:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('dob', models.CharField(max_length=100)),
                ('adress', models.TextField()),
                ('clgname', models.CharField(max_length=100)),
                ('clgyear', models.CharField(max_length=100)),
                ('clgcpi', models.CharField(max_length=100)),
                ('cls12name', models.CharField(max_length=100)),
                ('cls12year', models.IntegerField()),
                ('cls12cpi', models.CharField(max_length=100)),
                ('cls10name', models.CharField(max_length=100)),
                ('cls10year', models.IntegerField()),
                ('cls10cpi', models.CharField(max_length=100)),
                ('intrest', models.CharField(max_length=100)),
                ('planguages', models.CharField(max_length=100)),
                ('toolsandtech', models.CharField(max_length=100)),
                ('projectname', models.CharField(max_length=100)),
                ('projectguide', models.CharField(max_length=100)),
                ('projectdesc', models.TextField()),
                ('hobby1', models.CharField(max_length=100)),
                ('hobby2', models.CharField(max_length=100)),
                ('hobby3', models.CharField(max_length=100)),
                ('hobby4', models.CharField(max_length=100)),
            ],
        ),
    ]