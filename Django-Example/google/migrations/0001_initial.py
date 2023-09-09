# Generated by Django 4.2.4 on 2023-08-14 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_dtl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.EmailField(max_length=150, unique=True)),
                ('password', models.TextField(max_length=150, null=True)),
                ('type', models.TextField(max_length=15)),
                ('machine_id', models.TextField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_id', models.TextField(max_length=30)),
                ('status', models.TextField(max_length=20, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.ProtectedError, to='google.user_dtl')),
            ],
        ),
    ]
