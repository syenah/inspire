# Generated by Django 3.2.6 on 2021-08-04 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_project_stack'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='webpage',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
