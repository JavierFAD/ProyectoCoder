# Generated by Django 4.2 on 2023-06-29 00:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("herramienta", "0006_alter_herramienta_imagen"),
    ]

    operations = [
        migrations.AlterField(
            model_name="herramienta",
            name="imagen",
            field=models.ImageField(
                default="herramientas/herramienta.png", upload_to="herramientas"
            ),
        ),
    ]
