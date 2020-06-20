from django.shortcuts import render
from taxreader import readtax
from taxreader.models import CompanyTaxInfo
from django.http import JsonResponse, HttpResponse
from django.core import serializers
import json
from django.db.utils import IntegrityError


# Create your views here.

def index(request): 
    return render(request, 'taxreader/index.html')

def companies(request): 
    companies = CompanyTaxInfo.objects.all()
    context = {
        'companies':companies,
    }
    return render(request, 'taxreader/companies.html', context)

def get_tax_info(request):
    cui = request.GET['cui']
    date = request.GET['date']
    try:
        readtax.get_tax_info(cui,date)
    except(IntegrityError):
        print('IntegrityError')
    try:
        company = CompanyTaxInfo.objects.filter(cui=cui)
        json_company = serializers.serialize('json', company)
        print(company)
        print(len(company))
        if len(company) != 0:
            return HttpResponse(json_company, content_type="text/json-comment-filtered")
        else:
            return HttpResponse(False)
    except(ValueError):
        print('Value Error')
        return HttpResponse(False)
    


    
