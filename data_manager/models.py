from django.db import models


# Create your models here.

# Informazioa
class Taldea(models.Model):
    taldeIzena = models.CharField(max_length=255)
    liga = models.CharField(max_length=255)
    urtea = models.CharField(max_length=255)

class Estropada(models.Model):
    estropadaIzena = models.CharField(max_length=255)
    postua = models.CharField(max_length=255)
    taldeIzena = models.CharField(max_length=255)
    denbora = models.CharField(max_length=255)
    diferentzia = models.CharField(max_length=255)
    puntuak = models.CharField(max_length=255)
    liga = models.CharField(max_length=255)

class Egutegia(models.Model):
    estropadaZenbakia = models.CharField(max_length=255)
    estropadaIzena = models.CharField(max_length=255)
    lekua = models.CharField(max_length=255)
    eguna = models.CharField(max_length=255)
    liga = models.CharField(max_length=255)

# Erabiltzailearen atala
class Gremioa(models.Model):
    gremioIzena = models.CharField(max_length=255)
    pasahitza = models.CharField(max_length=255)
    gremioAdmin = models.CharField(max_length=255)

class Erabiltzailea(models.Model):
    erabiltzaileIzena = models.CharField(max_length=255)
    erabiltzaileAbizena = models.CharField(max_length=255)
    motea = models.CharField(max_length=255,primary_key=True)
    pasahitza = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    telefonoa = models.CharField(max_length=255)

class GremErab(models.Model):
    gremioIzena = models.CharField(max_length=255)
    motea = models.CharField(max_length=255)

class ErabPunt(models.Model):
    motea = models.CharField(max_length=255)
    liga = models.CharField(max_length=255)
    puntuak = models.IntegerField()

class Kiniela(models.Model):
    motea = models.CharField(max_length=255)
    estropadaIzena = models.CharField(max_length=255)
    bat = models.CharField(max_length=255)
    bi = models.CharField(max_length=255)
    hiru = models.CharField(max_length=255)
    lau = models.CharField(max_length=255)
    bost = models.CharField(max_length=255)
    sei = models.CharField(max_length=255)
    zazpi = models.CharField(max_length=255)
    zortzi = models.CharField(max_length=255)
    bederatzi = models.CharField(max_length=255)
    hamar = models.CharField(max_length=255)
    hamaika = models.CharField(max_length=255)
    hamabi = models.CharField(max_length=255)
    liga = models.CharField(max_length=255)
    puntuak = models.CharField(max_length=255)
