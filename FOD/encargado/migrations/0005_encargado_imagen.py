# Generated by Django 4.2 on 2023-06-27 01:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("encargado", "0004_alter_encargado_funcion"),
    ]

    operations = [
        migrations.AddField(
            model_name="encargado",
            name="imagen",
            field=models.ImageField(
                blank=True, default="encargado.jpg", null=True, upload_to="avatar"
            ),
        ),
    ]
