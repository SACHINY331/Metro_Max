# Generated by Django 4.2 on 2023-07-19 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='addres',
            field=models.TextField(),
        ),
    ]
