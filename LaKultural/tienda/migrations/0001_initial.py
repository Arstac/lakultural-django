# Generated by Django 4.1 on 2024-02-27 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CategoriaArticulo",
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
                ("nombre", models.CharField(max_length=100)),
                ("descripcion", models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="Producto",
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
                ("nombre", models.CharField(max_length=100)),
                ("descripcion", models.TextField()),
                ("imagen", models.ImageField(upload_to="productos/")),
                ("precio", models.DecimalField(decimal_places=2, max_digits=10)),
                ("stock", models.IntegerField(default=0)),
                ("activo", models.BooleanField(default=True)),
                (
                    "categoria",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="productos",
                        to="tienda.categoriaarticulo",
                    ),
                ),
            ],
        ),
    ]
