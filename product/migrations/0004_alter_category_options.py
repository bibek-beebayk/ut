# Generated by Django 5.0.3 on 2024-03-31 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0003_category_product"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "categories"},
        ),
    ]