# Generated by Django 4.0.3 on 2022-03-10 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Erabiltzailea',
            fields=[
                ('gremioIzena', models.CharField(max_length=255)),
                ('erabiltzaileIzena', models.CharField(max_length=255)),
                ('erabiltzaileAbizena', models.EmailField(max_length=254)),
                ('motea', models.EmailField(max_length=254)),
                ('pasahitza', models.EmailField(max_length=254)),
                ('puntuak', models.EmailField(max_length=254)),
            ],
        ),
    ]
