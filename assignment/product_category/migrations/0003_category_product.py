# Generated by Django 4.2 on 2023-07-19 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_category', '0002_remove_category_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='product',
            field=models.ManyToManyField(to='product_category.product'),
        ),
    ]
