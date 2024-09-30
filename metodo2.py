from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow,Flow
from google.auth.transport.requests import Request
from google.oauth2 import service_account
from datetime import date
from datetime import datetime
now = datetime.now()
format = now.strftime('%d/%m/%Y')
def exportarsheets(valor,columsale,columentra,pais,tasa,envio):
    file='python-sheets-bot-430619-5671d3cd4b52.json'
    Credentials=service_account.Credentials.from_service_account_file(filename=file)
    try:
       service = build('sheets', 'v4', credentials=Credentials)
       print(service)
    except:
       DISCOVERY_SERVICE_URL = 'https://sheets.googleapis.com/$discovery/rest?version=v4'
       service = build('sheets', 'v4', credentials=Credentials, discoveryServiceUrl=DISCOVERY_SERVICE_URL)
       print(service)
    ID='1NVID1OWnwz_vmXbU9HmQuB9OKF42KzvvZABi-PxbwlI'
    Name='REMESAS'
    indices=[[str(tasa)]]

    print(indices)
    #worksheet = service.spreadsheet.get_worksheet(0)
    print('voy a hacer la request para escribir')
    recibi=int(valor * -1)
    prueba=[[str(valor)]]
    pruebatwo=[[str(envio)]]
    values=[[format,pais]]
    result=service.spreadsheets().values().get(
    spreadsheetId=ID,

    range= 'B:N'

    ).execute()
    rows = result.get('values', [])
    next_row = len(rows) - 1
    print('{0} rows retrieved. 13'.format(len(rows)))
    resul=service.spreadsheets().values().append(
          spreadsheetId=ID,
          valueInputOption='USER_ENTERED',
          insertDataOption='INSERT_ROWS',
          range=f"B{next_row}:C{next_row}",
          body={'values':values}
    ).execute()
    resultados=service.spreadsheets().values().get(
    spreadsheetId=ID,

    range= 'B:N'

    ).execute()
    rowss = resultados.get('values', [])
    next_rows = len(rowss)
    print(next_rows)
    update=service.spreadsheets().values().update(
    spreadsheetId=ID, range=f"{columsale}{next_rows}",
    valueInputOption='USER_ENTERED', body={'values':prueba}).execute()

    resultadostwo=service.spreadsheets().values().get(
    spreadsheetId=ID,

    range= 'B:N'

    ).execute()
    rowsstwo = resultadostwo.get('values', [])
    next_rowstwo = len(rowsstwo)
    print(next_rowstwo)
    updatetwo=service.spreadsheets().values().update(
    spreadsheetId=ID, range=f"{columentra}{next_rowstwo}",
    valueInputOption='USER_ENTERED', body={'values':pruebatwo}).execute()

    resultadostre=service.spreadsheets().values().get(
    spreadsheetId=ID,

    range= 'B:N'

    ).execute()
    rowsstre = resultadostre.get('values', [])
    next_rowstre = len(rowsstre)
    print(next_rowstre)
    updatetre=service.spreadsheets().values().update(
    spreadsheetId=ID, range=f"D{next_rowstre}",
    valueInputOption='USER_ENTERED', body={'values':indices}).execute()

    print("Writing OK!!")
    #rows = result.get('values', [])
def retorna_tasas(colum,indice):
    retorna=None

    rangeName = f'TASAS!{colum}{indice}'
    file='python-sheets-bot-430619-5671d3cd4b52.json'
    Credentials=service_account.Credentials.from_service_account_file(filename=file)
    try:
       service = build('sheets', 'v4', credentials=Credentials)
       ID='1NVID1OWnwz_vmXbU9HmQuB9OKF42KzvvZABi-PxbwlI'

       result=service.spreadsheets().values().get(
       spreadsheetId=ID,
       range=rangeName
       ).execute()
       rows = result.get('values', [])
       print('{0} rows retrieved. 13'.format(len(rows)))
       for item in rows:
           for items in item:
               retorna=items
    except:

          DISCOVERY_SERVICE_URL = 'https://sheets.googleapis.com/$discovery/rest?version=v4'
          service = build('sheets', 'v4', credentials=Credentials, discoveryServiceUrl=DISCOVERY_SERVICE_URL)
          ID='1NVID1OWnwz_vmXbU9HmQuB9OKF42KzvvZABi-PxbwlI'
          result=service.spreadsheets().values().get(
          spreadsheetId=ID,
          range=rangeName
          ).execute()
          rows = result.get('values', [])
          print('{0} rows retrieved. 13'.format(len(rows)))
          for item in rows:
              for items in item:
                  retorna=items
    return retorna
def guarda_datos(user):
    rangeName ='B:T'
    file='python-sheets-bot-430619-5671d3cd4b52.json'
    Credentials=service_account.Credentials.from_service_account_file(filename=file)
    try:
       service = build('sheets', 'v4', credentials=Credentials)
       ID='1NVID1OWnwz_vmXbU9HmQuB9OKF42KzvvZABi-PxbwlI'
       result=service.spreadsheets().values().get(
       spreadsheetId=ID,
       range=rangeName
       ).execute()
       rows = result.get('values', [])
       print('{0} rows retrieved. 13'.format(len(rows)))
       next_row = len(rows)
       print(next_row)
       service.spreadsheets().values().update(
          spreadsheetId=ID,
          valueInputOption='USER_ENTERED',
          range=f'T{next_row}',
          body={'values':[[user]]}
       ).execute()

    except:

          DISCOVERY_SERVICE_URL = 'https://sheets.googleapis.com/$discovery/rest?version=v4'
          service = build('sheets', 'v4', credentials=Credentials, discoveryServiceUrl=DISCOVERY_SERVICE_URL)
          ID='1NVID1OWnwz_vmXbU9HmQuB9OKF42KzvvZABi-PxbwlI'
          result=service.spreadsheets().values().get(
          spreadsheetId=ID,
          range=rangeName
          ).execute()
          rows = result.get('values', [])
          print('{0} rows retrieved. 13'.format(len(rows)))
          next_row = len(rows)
          service.spreadsheets().values().update(
          spreadsheetId=ID,
          valueInputOption='USER_ENTERED',
          range=f'T{next_row}',
          body={'values':[[datos]]}
          ).execute()





