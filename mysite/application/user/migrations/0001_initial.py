# Generated by Django 2.0 on 2022-01-19 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('coutry', models.CharField(max_length=15)),
                ('Password', models.CharField(max_length=20)),
            ],
        ),
    ]
