# Generated by Django 3.0.6 on 2020-06-27 13:08

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_auto_20200627_1149'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='blogPost',
            new_name='Post',
        ),
    ]
