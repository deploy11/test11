# Generated by Django 4.2.6 on 2023-10-06 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_comment_javob_com'),
    ]

    operations = [
        migrations.RenameField(
            model_name='javob',
            old_name='com',
            new_name='comment',
        ),
    ]
