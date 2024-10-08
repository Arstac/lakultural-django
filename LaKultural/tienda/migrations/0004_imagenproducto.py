# Generated by Django 4.1 on 2024-05-04 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tienda", "0003_alter_producto_tallas"),
    ]

    operations = [
        migrations.CreateModel(
            name="ImagenProducto",
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
                ("imagen", models.ImageField(upload_to="imagenes_productos/")),
                (
                    "producto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="imagenes",
                        to="tienda.producto",
                    ),
                ),
            ],
        ),
    ]
