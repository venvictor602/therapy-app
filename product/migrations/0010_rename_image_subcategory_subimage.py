# Generated by Django 4.0.5 on 2023-07-10 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_category_image_subcategory_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcategory',
            old_name='image',
            new_name='subimage',
        ),
    ]
