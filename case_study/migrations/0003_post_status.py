# Generated by Django 3.2 on 2022-02-27 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case_study', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0),
        ),
    ]
