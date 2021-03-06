# Generated by Django 3.2.6 on 2021-09-12 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_author_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_image',
            field=models.ImageField(default='nothing', upload_to='posts'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='author',
            name='photo',
            field=models.ImageField(upload_to='authors'),
        ),
    ]
