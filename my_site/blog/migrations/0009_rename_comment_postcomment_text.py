# Generated by Django 3.2.6 on 2021-09-12 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_postcomment_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postcomment',
            old_name='comment',
            new_name='text',
        ),
    ]