# Generated by Django 4.0.5 on 2023-07-10 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_rename_icon_title_category_photo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='photo',
        ),
    ]
