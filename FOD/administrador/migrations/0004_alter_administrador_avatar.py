# Generated by Django 4.2 on 2023-06-29 23:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("administrador", "0003_alter_administrador_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="administrador",
            name="avatar",
            field=models.ImageField(blank=True, null=True, upload_to="avatares"),
        ),
    ]
