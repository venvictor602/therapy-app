# Generated by Django 4.0.5 on 2023-07-10 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_remove_category_photo_remove_subcategory_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='book_date',
        ),
    ]
