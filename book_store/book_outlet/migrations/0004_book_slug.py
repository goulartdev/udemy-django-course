# Generated by Django 3.2.6 on 2021-09-02 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0003_rename_is_bestselling_book_is_bestseller'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(default='', max_length=80),
        ),
    ]
