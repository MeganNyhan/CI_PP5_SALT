# Generated by Django 3.2 on 2022-07-13 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='featured_image',
        ),
    ]