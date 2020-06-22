from django.shortcuts import render
from taxreader import readtax
from taxreader.models import CompanyTaxInfo, ResponseFromAnaf
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.core import serializers
import json
from django.db.utils import IntegrityError
from django.forms.models import model_to_dict
from django.urls import reverse




# Create your views here.

def index(request): 
    return render(request, 'taxreader/index.html')

def companies(request): 
    companies = CompanyTaxInfo.objects.all()
    context = {
        'companies':companies,
    }
    return render(request, 'taxreader/companies.html', context)

def all_responses(request): 
    responses = ResponseFromAnaf.objects.all()
    context = {
        'responses':responses,
    }
    return render(request, 'taxreader/allresponses.html', context)

def clear_responses(request): 
    ResponseFromAnaf.objects.all().delete()
    return HttpResponseRedirect(reverse('all_responses'))

def clear_companies(request): 
    CompanyTaxInfo.objects.all().delete()
    return HttpResponseRedirect(reverse('companies'))

def get_tax_info(request):
    cui = request.GET['cui']
    date = request.GET['date']
    try:
        CompanyTaxInfo.objects.filter(cui=cui, data=date).delete()
    except:
        pass
    try:
        readtax.get_tax_info(cui,date)
    except(IntegrityError):
        print('IntegrityError')
    try:
        company = CompanyTaxInfo.objects.filter(cui=cui, data=date)
        json_company = serializers.serialize('json', company)
        if len(company) != 0:
            return HttpResponse(json_company, content_type="text/json-comment-filtered")
        else:
            return HttpResponse(False)
    except(ValueError):
        print('Value Error')
        return HttpResponse(False)

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')


    
