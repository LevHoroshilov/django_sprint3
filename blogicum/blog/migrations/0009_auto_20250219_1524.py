# Generated by Django 3.2.16 on 2025-02-19 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20250219_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default='<built-in method today of type object at 0x1015ba9d0>'),
        ),
        migrations.AlterField(
            model_name='location',
            name='created_at',
            field=models.DateTimeField(default='<built-in method today of type object at 0x1015ba9d0>'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default='<built-in method today of type object at 0x1015ba9d0>'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default='<built-in method today of type object at 0x1015ba9d0>'),
        ),
    ]
