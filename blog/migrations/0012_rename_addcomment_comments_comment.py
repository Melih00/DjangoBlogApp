# Generated by Django 3.2.8 on 2021-10-26 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_rename_content_comments_addcomment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='addcomment',
            new_name='comment',
        ),
    ]
