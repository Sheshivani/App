# Generated by Django 3.1 on 2020-09-08 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='comments',
            field=models.ManyToManyField(blank=True, null=True, to='app.Comment'),
        ),
    ]
