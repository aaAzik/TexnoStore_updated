# Generated by Django 4.2.3 on 2023-08-08 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoop', '0002_remove_category_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='author',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=999),
        ),
    ]
