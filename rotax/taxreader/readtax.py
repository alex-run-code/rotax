import requests
from taxreader.models import CompanyTaxInfo

def get_tax_info(cui, date):
    post = [{"cui": cui, "data":date }]
    re = requests.post('https://webservicesp.anaf.ro/PlatitorTvaRest/api/v4/ws/tva', json=post)
    json_response = re.json()
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


#  response example:
# {
#   "cod": 200,
#   "message": "SUCCESS",
#   "found": [
#     {
#       "cui": 33811173,
#       "data": "2014-11-17",
#       "denumire": "KODING TECHNOLOGY SRL",
#       "adresa": "MUNICIPIUL BUCUREÅžTI, SECTOR 6, STR. ERNEST JUVARA, NR.16, ET.3",
#       "scpTVA": false,
#       "data_inceput_ScpTVA": " ",
#       "data_sfarsit_ScpTVA": " ",
#       "data_anul_imp_ScpTVA": " ",
#       "mesaj_ScpTVA": "neplatitor IN SCOPURI de TVA la data cautata",
#       "dataInceputTvaInc": "",
#       "dataSfarsitTvaInc": "",
#       "dataActualizareTvaInc": "",
#       "dataPublicareTvaInc": "",
#       "tipActTvaInc": "",
#       "statusTvaIncasare": false,
#       "dataInactivare": " ",
#       "dataReactivare": " ",
#       "dataPublicare": " ",
#       "dataRadiere": " ",
#       "statusInactivi": false,
#       "dataInceputSplitTVA": "",
#       "dataAnulareSplitTVA": "",
#       "statusSplitTVA": false,
#       "iban": ""
#     }
#   ],
#   "notfound": []
# }