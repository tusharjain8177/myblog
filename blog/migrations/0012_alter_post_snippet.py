# Generated by Django 4.0.6 on 2022-08-29 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click The Above Like To Read This post...', max_length=200),
        ),
    ]
