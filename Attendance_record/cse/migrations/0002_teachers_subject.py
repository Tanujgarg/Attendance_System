# Generated by Django 2.0.1 on 2018-02-03 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cse', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachers',
            name='subject',
            field=models.CharField(default=None, max_length=255),
        ),
    ]