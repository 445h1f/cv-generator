# Generated by Django 4.2.7 on 2023-12-01 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_pdf', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]
