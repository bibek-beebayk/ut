# Generated by Django 5.0.3 on 2024-04-02 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0007_alter_contactus_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="contactus",
            name="is_addressed",
            field=models.BooleanField(default=False),
        ),
    ]