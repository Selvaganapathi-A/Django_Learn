# Generated by Django 4.2b1 on 2023-03-15 03:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("learn", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="venue",
            name="picture",
            field=models.ImageField(
                blank=True,
                default=None,
                null=True,
                upload_to="venue",
                verbose_name="Venue Picture",
            ),
        ),
    ]
