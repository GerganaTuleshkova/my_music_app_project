# Generated by Django 4.0.2 on 2022-02-27 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ['pk']},
        ),
    ]
