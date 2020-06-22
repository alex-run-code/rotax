import requests
from taxreader.models import CompanyTaxInfo, ResponseFromAnaf
import datetime

def get_tax_info(cui, date):
    post = [{"cui": cui, "data":date }]
    re = requests.post('https://webservicesp.anaf.ro/PlatitorTvaRest/api/v4/ws/tva', json=post)
    if re.status_code == 200:
        json_response = re.json()
        print(json_response['found'][0]['denumire'])
        print(len(json_response['found'][0]['denumire']))
        new_response_from_anaf = ResponseFromAnaf(
            date = datetime.datetime.now(),
            data_sent = post,
            data_received = json_response,
            status_code = 200,
        )
        new_response_from_anaf.save()
        if len(json_response['found'][0]['denumire']) != 0:
            cui = json_response['found'][0]['cui']
            new_company = CompanyTaxInfo(
                cui=json_response['found'][0]['cui'],
                data=json_response['found'][0]['data'],
                denumire=json_response['found'][0]['denumire'],
                adresa=json_response['found'][0]['adresa'],
                data_inceput_ScpTVA=json_response['found'][0]['data_inceput_ScpTVA'],
                data_sfarsit_ScpTVA=json_response['found'][0]['data_sfarsit_ScpTVA'],
                data_anul_imp_ScpTVA=json_response['found'][0]['data_anul_imp_ScpTVA'],
                mesaj_ScpTVA=json_response['found'][0]['mesaj_ScpTVA'],
                dataInceputTvaInc=json_response['found'][0]['dataInceputTvaInc'],
                dataSfarsitTvaInc=json_response['found'][0]['dataSfarsitTvaInc'],
                dataActualizareTvaInc=json_response['found'][0]['dataActualizareTvaInc'],
                dataPublicareTvaInc=json_response['found'][0]['dataPublicareTvaInc'],
                tipActTvaInc=json_response['found'][0]['tipActTvaInc'],
                statusTvaIncasare=json_response['found'][0]['statusTvaIncasare'],
                dataInactivare=json_response['found'][0]['dataInactivare'],
                dataReactivare=json_response['found'][0]['dataReactivare'],
                dataPublicare=json_response['found'][0]['dataPublicare'],
                dataRadiere=json_response['found'][0]['dataRadiere'],
                statusInactivi=json_response['found'][0]['statusInactivi'],
                dataInceputSplitTVA=json_response['found'][0]['dataInceputSplitTVA'],
                dataAnulareSplitTVA=json_response['found'][0]['dataAnulareSplitTVA'],
                statusSplitTVA=json_response['found'][0]['statusSplitTVA'],
                iban=json_response['found'][0]['iban'],
            )
            new_company.save()
            print(json_response['found'][0]['denumire'], ' - added')
    else:
        new_response_from_anaf = ResponseFromAnaf(
            date = datetime.datetime.now(),
            data_sent = post,
            data_received = 'None',
            status_code = 500,
        )
        new_response_from_anaf.save()
        return(False)
