# Generated by Django 3.2.25 on 2024-11-21 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20241106_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='visibilty',
            field=models.BooleanField(default=True),
        ),
    ]
