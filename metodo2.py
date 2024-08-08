from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow,Flow
from google.auth.transport.requests import Request
from google.oauth2 import service_account
from datetime import date
from datetime import datetime
now = datetime.now()
format = now.strftime('%d/%m/%Y')
def exportarsheets(valor,colum,pais,tasa):
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
    indices=tasa
    #worksheet = service.spreadsheet.get_worksheet(0)
    print('voy a hacer la request para escribir')
    prueba=[[str(valor)]]
    values=[[format,pais,int(indices)]] 
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
    spreadsheetId=ID, range=f"{colum}{next_rows}",
    valueInputOption='USER_ENTERED', body={'values':prueba}).execute()

    print("Writing OK!!")
    #rows = result.get('values', [])