# Generated by Django 3.2.5 on 2021-07-19 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_postmodel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='like',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
