# Generated by Django 3.2 on 2024-11-04 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'default_related_name': 'comments'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'default_related_name': 'posts'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=30),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(max_length=30),
        ),
    ]
