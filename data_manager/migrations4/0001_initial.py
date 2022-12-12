# Generated by Django 4.0.3 on 2022-11-07 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Egutegia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estropadaZenbakia', models.CharField(max_length=255)),
                ('estropadaIzena', models.CharField(max_length=255)),
                ('lekua', models.CharField(max_length=255)),
                ('eguna', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Erabiltzailea',
            fields=[
                ('erabiltzaileIzena', models.CharField(max_length=255)),
                ('erabiltzaileAbizena', models.CharField(max_length=255)),
                ('motea', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('pasahitza', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Estropada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estropadaIzena', models.CharField(max_length=255)),
                ('postua', models.CharField(max_length=255)),
                ('taldeIzena', models.CharField(max_length=255)),
                ('denbora', models.CharField(max_length=255)),
                ('diferentzia', models.CharField(max_length=255)),
                ('puntuak', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='GremErab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gremioIzena', models.CharField(max_length=255)),
                ('motea', models.CharField(max_length=255)),
                ('puntuak', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Gremioa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gremioIzena', models.CharField(max_length=255)),
                ('pasahitza', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Kiniela',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gremioIzena', models.CharField(max_length=255)),
                ('motea', models.CharField(max_length=255)),
                ('estropadaIzena', models.CharField(max_length=255)),
                ('bat', models.CharField(max_length=255)),
                ('bi', models.CharField(max_length=255)),
                ('hiru', models.CharField(max_length=255)),
                ('lau', models.CharField(max_length=255)),
                ('bost', models.CharField(max_length=255)),
                ('sei', models.CharField(max_length=255)),
                ('zazpi', models.CharField(max_length=255)),
                ('zortzi', models.CharField(max_length=255)),
                ('bederatzi', models.CharField(max_length=255)),
                ('hamar', models.CharField(max_length=255)),
                ('hamaika', models.CharField(max_length=255)),
                ('hamabi', models.CharField(max_length=255)),
                ('puntuak', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Taldea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taldeIzena', models.CharField(max_length=255)),
                ('urtea', models.CharField(max_length=255)),
            ],
        ),
    ]
