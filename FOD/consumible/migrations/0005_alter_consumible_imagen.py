# Generated by Django 4.2 on 2023-06-29 00:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("consumible", "0004_alter_consumible_imagen"),
    ]

    operations = [
        migrations.AlterField(
            model_name="consumible",
            name="imagen",
            field=models.ImageField(
                blank=True, default="consumible.png", null=True, upload_to="consumibles"
            ),
        ),
    ]