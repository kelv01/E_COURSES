# Generated by Django 5.0 on 2024-07-26 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='courseName',
            field=models.CharField(max_length=100),
        ),
    ]
