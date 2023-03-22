# Generated by Django 4.1.7 on 2023-03-22 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='programmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=3)),
                ('brirthday', models.DateField()),
                ('score', models.PositiveSmallIntegerField()),
            ],
            options={
                'db_table': 'programmer',
            },
        ),
    ]
