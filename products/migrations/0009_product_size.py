# Generated by Django 3.2 on 2022-07-18 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20220718_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
