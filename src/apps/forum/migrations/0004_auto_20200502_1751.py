# Generated by Django 3.0.5 on 2020-05-02 14:51

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tickets', '0010_auto_20200420_2303'),
        ('forum', '0003_auto_20200502_1746'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ForumComment',
            new_name='Comment',
        ),
    ]