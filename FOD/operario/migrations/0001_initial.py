# Generated by Django 4.2 on 2023-06-20 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("encargado", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Operario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nombre",
                    models.CharField(blank=True, default="", max_length=80, null=True),
                ),
                ("apellido", models.CharField(max_length=60)),
                ("legajo", models.IntegerField()),
                ("funcion", models.TextField()),
                (
                    "encargado",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="encargado.encargado",
                    ),
                ),
            ],
        ),
    ]