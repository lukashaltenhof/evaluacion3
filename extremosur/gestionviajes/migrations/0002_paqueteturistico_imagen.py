# Generated by Django 4.1.2 on 2024-07-18 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionviajes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paqueteturistico',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes_paquetes/'),
        ),
    ]
