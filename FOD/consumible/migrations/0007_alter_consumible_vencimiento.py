# Generated by Django 4.2 on 2023-07-02 02:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("consumible", "0006_alter_consumible_descripcion_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="consumible",
            name="vencimiento",
            field=models.DateField(blank=True, help_text="Formato dd/mm/aa", null=True),
        ),
    ]