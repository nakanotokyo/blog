# Generated by Django 4.0.2 on 2022-07-04 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_tag_alter_category_slug_alter_post_category_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tags',
            new_name='tag',
        ),
    ]
