# Generated by Django 5.1.4 on 2025-03-01 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_tag_icon_tag_is_active_tag_title_alter_tag_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='title',
            new_name='description',
        ),
    ]
