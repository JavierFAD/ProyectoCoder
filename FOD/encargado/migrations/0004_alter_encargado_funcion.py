# Generated by Django 4.2 on 2023-06-27 00:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("encargado", "0003_remove_encargado_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="encargado",
            name="funcion",
            field=models.CharField(max_length=100, verbose_name="Función"),
        ),
    ]
