from django.db import models

# Create your models here.


class CompanyTaxInfo(models.Model):
    cui = models.IntegerField(unique=True)
    data =  models.CharField(max_length=1000)
    denumire= models.CharField(max_length=100)
    adresa = models.CharField(max_length=1000)
    scpTVA = models.BooleanField(null=True)
    data_inceput_ScpTVA = models.CharField(max_length=1000)
    data_sfarsit_ScpTVA = models.CharField(max_length=1000)
    data_anul_imp_ScpTVA = models.CharField(max_length=1000)
    mesaj_ScpTVA = models.CharField(max_length=1000)
    dataInceputTvaInc = models.CharField(max_length=1000)
    dataSfarsitTvaInc = models.CharField(max_length=1000)
    dataActualizareTvaInc = models.CharField(max_length=1000)
    dataPublicareTvaInc = models.CharField(max_length=1000)
    tipActTvaInc = models.CharField(max_length=1000)
    statusTvaIncasare =  models.BooleanField(null=True)
    dataInactivare = models.CharField(max_length=1000)
    dataReactivare = models.CharField(max_length=1000)
    dataPublicare = models.CharField(max_length=1000)
    dataRadiere = models.CharField(max_length=1000)
    statusInactivi = models.BooleanField(null=True)
    dataInceputSplitTVA = models.CharField(max_length=1000)
    dataAnulareSplitTVA = models.CharField(max_length=1000)
    statusSplitTVA = models.BooleanField(null=True)
    iban = models.CharField(max_length=100)