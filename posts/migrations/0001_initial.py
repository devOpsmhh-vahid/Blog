# Generated by Django 3.2.5 on 2021-07-14 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('txt', models.TextField(blank=True, max_length=500, null=True)),
                ('img', models.ImageField(null=True, upload_to='')),
                ('like', models.IntegerField(default=0)),
                ('post_type', models.CharField(choices=[(1, 'post'), (2, 'repost')], default=1, max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.postmodel')),
            ],
        ),
    ]
