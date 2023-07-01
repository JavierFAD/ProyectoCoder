# Generated by Django 4.2 on 2023-06-27 00:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("herramienta", "0003_alter_herramienta_asignado_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="herramienta",
            name="calibracion",
            field=models.DateField(
                blank=True,
                help_text="Formato = mm/dd/aaaa",
                null=True,
                verbose_name="Fecha de Calibración",
            ),
        ),
        migrations.AlterField(
            model_name="herramienta",
            name="descripcion",
            field=models.TextField(verbose_name="Descripción"),
        ),
    ]