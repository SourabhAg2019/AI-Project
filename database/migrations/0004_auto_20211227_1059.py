# Generated by Django 2.2.12 on 2021-12-27 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_auto_20211227_0711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaintrecord',
            name='Status',
            field=models.CharField(choices=[('Not seen', 'Not seen'), ('seen', 'seen')], default='Not seen', max_length=20),
        ),
    ]