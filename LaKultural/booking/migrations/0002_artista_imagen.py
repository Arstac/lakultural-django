# Generated by Django 4.1 on 2024-03-02 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="artista",
            name="imagen",
            field=models.ImageField(blank=True, null=True, upload_to="booking/fotos/"),
        ),
    ]
