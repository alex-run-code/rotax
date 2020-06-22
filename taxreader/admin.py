from django.contrib import admin
from taxreader.models import CompanyTaxInfo, ResponseFromAnaf
# Register your models here.
admin.site.register(CompanyTaxInfo)
admin.site.register(ResponseFromAnaf)