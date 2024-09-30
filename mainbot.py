import telebot
from telebot.types import ReplyKeyboardMarkup , KeyboardButton, InlineKeyboardMarkup, Update, InlineKeyboardButton
import requests
import threading
from telebot import types
from metodo2 import exportarsheets,retorna_tasas,guarda_datos
from datetime import date
from datetime import datetime
import json,os
from threading import Thread
bot = telebot.TeleBot("7314835560:AAEijFpKshQbVyNgolYp887Uzi9lG0MFb5Q",threaded=False)
#bot = AsyncTeleBot("7314835560:AAEijFpKshQbVyNgolYp887Uzi9lG0MFb5Q", parse_mode=None)
hideBoard = types.ReplyKeyboardRemove()
admin=[]
clientes=[]
votaciones=[]
pedidos=[]
text_pedidos={}
clientes_step={}
nombre={}
destinos={}
envios={}
tasastwo={}
letrastwo={}
entradastwo={}
destino=[]
tasa=[]
origen=[]
letra=[]
denominacion=[]
envio=[]
threads = []
users=[]
pedidos=[]
def transaccion(user,tipo):
	archivo=open("datosuser.txt",'r')
	for line in archivo.readlines():
		tokens=str.split(line," ")
		if tokens[0] == "clientes":
		    if tokens[1] == str(user) and tipo == "destinos":
		       return tokens[3]
		    elif tokens[1] == str(user) and tipo == "envios":
		       return tokens[4]
		    elif tokens[1] == str(user) and tipo == "tasas":
		        return tokens[5]
		    elif tokens[1] == str(user) and tipo == "letras":
		        return tokens[6]
		    elif tokens[1] == str(user) and tipo == "entradas":
		        return tokens[5]
		    elif tokens[1] == str(user) and tipo == "envia":
		        return tokens[2]

	archivo.close()

def Guardartxt():
    files=open("datosuser.txt",'w')
    for item in pedidos:
        print(item)
        files.write("clientes "+str(item)+" "+str(nombre[item])+" "+str(destinos[item])+" "+str(envios[item])+" "+str(entradastwo[item])+" "+str(letrastwo[item])+" "+str(entradastwo[item])+"\n")
    files.close()

def Guardar():
	file=open("users.txt",'w')
	for item in users:

		file.write("clientes "+str(item)+"\n")

	file.close()
def Cargar(user):
	file=open("users.txt",'r')
	for line in file.readlines():
		tokens=str.split(line," ")
		if tokens[0]=="clientes":

		   print('es')
		   if int(tokens[1])==(user):

		       return tokens[1]

	file.close()





def count(message):

    markup = InlineKeyboardMarkup(row_width=4)
    var1 = InlineKeyboardButton("ARGENTINA",callback_data="ARGENTINA")
    var2 = InlineKeyboardButton("BRASIL", callback_data="BRASIL")
    var3 = InlineKeyboardButton("CHILE",callback_data="CHILE")
    var4 = InlineKeyboardButton("ESPAÑA",callback_data="ESPAÑA")
    var5 = InlineKeyboardButton("EEUU", callback_data="EEUU")
    var6 = InlineKeyboardButton("USA",callback_data="USA")
    var7 = InlineKeyboardButton("PANAMA",callback_data="PANAMA")
    var8 = InlineKeyboardButton("PERU", callback_data="PERU")
    var9 = InlineKeyboardButton("USDT",callback_data="USDT")
    var10 = InlineKeyboardButton("VENEZUELA",callback_data="VENEZUELA")
    var11 = InlineKeyboardButton("CERRAR",callback_data="CERRAR")
    markup.add(var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11)
    bot.send_message(message.from_user.id,"Bienvenido a nuestra casa de cambio IBG,nuestros bots con inteligencia artificial seran los encargados de atenderlo,LOS PAISES CON LOS QUE TRABAJAMOS SE MUESTRAN A CONTINUACION, POR FAVOR PULSE EL PAIS DESDE DONDE ENVIA..." ,reply_markup=markup)
    users.append(message.from_user.id)
    Guardar()
def respuesta_botones_inline(call):
    cid=call.from_user.id
    mid=call.message.id
    if call.data == "CERRAR" :
        bot.delete_message(cid,mid)

    elif call.data == "ARGENTINA" :
         bot.send_message(cid,"HAGA CLICK HACIA DONDE DESEA ENVIAR /ARGENTINA_BRASIL /ARGENTINA_CHILE /ARGENTINA_ESPANA /ARGENTINA_EEUU /ARGENTINA_USA /ARGENTINA_PANAMA /ARGENTINA_PERU /ARGENTINA_USDT /ARGENTINA_VENEZUELA",reply_markup=hideBoard)
    elif call.data == "BRASIL" :
         bot.send_message(cid,"HAGA CLICK HACIA DONDE DESEA ENVIAR /BRASIL_ARGENTINA /BRASIL_CHILE /BRASIL_ESPANA /BRASIL_EEUU /BRASIL_USA /BRASIL_PANAMA /BRASIL_PERU /BRASIL_USDT /BRASIL_VENEZUELA",reply_markup=hideBoard)
    elif call.data == "CHILE" :
         bot.send_message(cid,"HAGA CLICK HACIA DONDE DESEA ENVIAR /CHILE_BRASIL /CHILE_ARGENTINA /CHILE_ESPANA /CHILE_EEUU /CHILE_USA /CHILE_PANAMA /CHILE_PERU /CHILE_USDT /CHILE_VENEZUELA",reply_markup=hideBoard)
    elif call.data == "ESPAÑA" :
         bot.send_message(cid,"HAGA CLICK HACIA DONDE DESEA ENVIAR /ESPANA_BRASIL /ESPANA_ARGENTINA /ESPANA_CHILE /ESPANA_EEUU /ESPANA_USA /ESPANA_PANAMA /ESPANA_PERU /ESPANA_USDT /ESPANA_VENEZUELA",reply_markup=hideBoard)
    elif call.data == "EEUU" :
         bot.send_message(cid,"HAGA CLICK HACIA DONDE DESEA ENVIAR /EEUU_ARGENTINA /EEUU_BRASIL /EEUU_CHILE /EEUU_ESPANA /EEUU_USA /EEUU_PANAMA /EEUU_PERU /EEUU_USDT /EEUU_VENEZUELA",reply_markup=hideBoard)
    elif call.data == "USA" :
         bot.send_message(cid,"HAGA CLICK HACIA DONDE DESEA ENVIAR /USA_ARGENTINA /USA_BRASIL /USA_CHILE /USA_ESPANA /USA_EEUU  /USA_PANAMA /USA_PERU /USA_USDT /USA_VENEZUELA",reply_markup=hideBoard)
    elif call.data == "PANAMA" :
         bot.send_message(cid,"HAGA CLICK HACIA DONDE DESEA ENVIAR /PANAMA_ARGENTINA /PANAMA_BRASIL /PANAMA_CHILE /PANAMA_ESPANA /PANAMA_EEUU /PANAMA_USA /PANAMA_PERU /PANAMA_USDT /PANAMA_VENEZUELA",reply_markup=hideBoard)
    elif call.data == "PERU" :
         bot.send_message(cid,"HAGA CLICK HACIA DONDE DESEA ENVIAR /PERU_ARGENTINA /PERU_BRASIL /PERU_CHILE /PERU_ESPANA /PERU_EEUU /PERU_USA /PERU_PANAMA /PERU_USDT /PERU_VENEZUELA",reply_markup=hideBoard)
    elif call.data == "USDT" :
         bot.send_message(cid,"HAGA CLICK HACIA DONDE DESEA ENVIAR /USDT_ARGENTINA /USDT_BRASIL /USDT_CHILE /USDT_ESPANA /USDT_EEUU /USDT_USA /USDT_PANAMA /USDT_PERU /USDT_VENEZUELA",reply_markup=hideBoard)
    elif call.data == "VENEZUELA" :
         bot.send_message(cid,"HAGA CLICK HACIA DONDE DESEA ENVIAR /VENEZUELA_ARGENTINA /VENEZUELA_BRASIL /VENEZUELA_CHILE /VENEZUELA_ESPANA /VENEZUELA_EEUU /VENEZUELA_USA /VENEZUELA_PANAMA /VENEZUELA_PERU /VENEZUELA_USDT",reply_markup=hideBoard)

#region envio desde argentina

def cantidadAB(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/ARGENTINA_BRASIL':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid,transaccionAB)
def transaccionAB(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('E',28))
    try:
        usuarios=Cargar(cid)
        print(cid)
        if int(usuarios) == cid:
           entrada = float(entrada)
           total=(float(entrada)*tasas)
           clientes.append(-total)
           destino.append('BRASIL')
           origen.append('ARGENTINA')
           letra.append('I')
           tasa.append(tasas)
           envio.append(float(entrada))
           pedidos.append(m.from_user.id)
           nombre[cid]=entrada
           destinos[cid]="BRASIL"
           envios[cid]="ARGENTINA"
           tasastwo[cid]=tasas
           letrastwo[cid]="I"
           entradastwo[cid]=total
           Guardartxt()
           bot.send_message(cid,"La tasa de cambio para Brasil es de "+ str(tasas) +" Reais por peso argentino, usted recibira un total de:"+ str(total) +" reais, pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")

    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid,transaccionAB)

def cantidadAC(message):
     cid = message.from_user.id
     print('entro')
     nombre=message.text
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/ARGENTINA_CHILE':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar . ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionAC)
def transaccionAC(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('E',26))
    try:
        usuarios=Cargar(cid)
        print(cid)
        if int(usuarios) == cid:
           entrada = float(entrada)
           total=(float(entrada)*tasas)
           print(total)
           clientes.append(-total)
           destino.append('CHILE')
           origen.append('ARGENTINA')
           letra.append('I')
           tasa.append(tasas)
           envio.append(float(entrada))
           pedidos.append(m.from_user.id)
           nombre[cid]=entrada
           destinos[cid]="CHILE"
           envios[cid]="ARGENTINA"
           tasastwo[cid]=tasas
           letrastwo[cid]="I"
           entradastwo[cid]=total
           Guardartxt()
           bot.send_message(cid,"La tasa de cambio para Chile  es de "+ str(tasas) +" Peso chileno por peso argentino, usted recibira un total de:"+ str(total) +" pesos, pulse el comando /Procesar o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionAC)
@bot.message_handler(commands=['ARGENTINA_ESPANA'])
def cantidadAES(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/ARGENTINA_ESPANA':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar . ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionAES)
def transaccionAES(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('E',36))
    try:
        usuarios=Cargar(cid)
        print(cid)
        if int(usuarios) == cid:
         entrada = float(entrada)
         total=(float(entrada)*tasas)
         print(total)
         clientes.append(-total)
         tasa.append(tasas)
         origen.append('ARGENTINA')
         destino.append('ESPAÑA')
         letra.append('I')
         envio.append(float(entrada))
         pedidos.append(m.from_user.id)
         nombre[cid]=entrada
         destinos[cid]="ESPAÑA"
         envios[cid]="ARGENTINA"
         tasastwo[cid]=tasas
         letrastwo[cid]="I"
         entradastwo[cid]=total
         Guardartxt()
         bot.send_message(cid,"La tasa de cambio para España  es de  "+ str(tasas) +"  Euro por peso argentino, usted recibira un total de:"+ str(total) +" euros, pulse el comando /Procesar o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionAES)
@bot.message_handler(commands=['ARGENTINA_EEUU'])
def cantidadAEU(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/ARGENTINA_EEUU':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionAEU)
def transaccionAEU(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('E',32))
    try:
        usuarios=Cargar(cid)
        print(cid)
        if int(usuarios) == cid:
         entrada = float(entrada)
         total=(float(entrada)*tasas)
         print(total)
         tasa.append(tasas)
         clientes.append(-total)
         destino.append('EEUU')
         origen.append('ARGENTINA')
         letra.append('I')
         envio.append(float(entrada))
         pedidos.append(m.from_user.id)
         nombre[cid]=entrada
         destinos[cid]="EEUU"
         envios[cid]="ARGENTINA"
         tasastwo[cid]=tasas
         letrastwo[cid]="I"
         entradastwo[cid]=total
         Guardartxt()
         bot.send_message(cid,"La tasa de cambio para EEUU  es de   "+ str(tasas) +"   Dolares por peso argentino, usted recibira un total de:"+ str(total) +" dolares, pulse el comando /Procesar o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionAEU)
@bot.message_handler(commands=['ARGENTINA_USA'])
def cantidadAUS(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/ARGENTINA_USA':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionAUS)
def transaccionAUS(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('E',32))
    try:
        usuarios=Cargar(cid)
        print(cid)
        if int(usuarios) == cid:
         entrada = float(entrada)
         total=(float(entrada)*tasas)
         print(total)
         tasa.append(tasas)
         clientes.append(-total)
         destino.append('USA')
         origen.append('ARGENTINA')
         letra.append('I')
         envio.append(float(entrada))
         pedidos.append(m.from_user.id)
         nombre[cid]=entrada
         destinos[cid]="USA"
         envios[cid]="ARGENTINA"
         tasastwo[cid]=tasas
         letrastwo[cid]="I"
         entradastwo[cid]=total
         Guardartxt()
         bot.send_message(cid,"La tasa de cambio para USA  es de  "+ str(tasas) +"  Dolares por peso argentino, usted recibira un total de:"+ str(total) +" dolares, pulse el comando /Procesar o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionAUS)
@bot.message_handler(commands=['ARGENTINA_PANAMA'])
def cantidadAPAN(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/ARGENTINA_PANAMA':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionAPAN)
def transaccionAPAN(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('E',30))
    try:
        usuarios=Cargar(cid)
        print(cid)
        if int(usuarios) == cid:
         entrada = float(entrada)
         total=(float(entrada)*tasas)
         print(total)
         tasa.append(tasas)
         clientes.append(-total)
         destino.append('PANAMA')
         origen.append('ARGENTINA')
         letra.append('I')
         envio.append(float(entrada))
         pedidos.append(m.from_user.id)
         nombre[cid]=entrada
         destinos[cid]="PANAMA"
         envios[cid]="ARGENTINA"
         tasastwo[cid]=tasas
         letrastwo[cid]="I"
         entradastwo[cid]=total
         Guardartxt()
         bot.send_message(cid,"La tasa de cambio para Panama  es de "+ str(tasas) +" Dolar Panama por peso argentino, usted recibira un total de:"+ str(total) +" , pulse el comando /Procesar o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionAPAN)
@bot.message_handler(commands=['ARGENTINA_PERU'])
def cantidadAPER(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/ARGENTINA_PERU':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionAPER)
def transaccionAPER(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('E',24))
    try:
        usuarios=Cargar(cid)
        print(cid)
        if int(usuarios) == cid:
         entrada = float(entrada)
         total=(float(entrada)*tasas)
         print(total)
         tasa.append(tasas)
         clientes.append(-total)
         destino.append('PERU')
         origen.append('ARGENTINA')
         letra.append('I')
         envio.append(float(entrada))
         pedidos.append(m.from_user.id)
         nombre[cid]=entrada
         destinos[cid]="PERU"
         envios[cid]="ARGENTINA"
         tasastwo[cid]=tasas
         letrastwo[cid]="I"
         entradastwo[cid]=total
         Guardartxt()
         bot.send_message(cid,"La tasa de cambio para Peru  es de  "+ str(tasas) +"  Soles por peso argentino, usted recibira un total de:"+ str(total) +" soles, pulse el comando /Procesar o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionAPER)
@bot.message_handler(commands=['ARGENTINA_USDT'])
def cantidadAUSDT(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/ARGENTINA_USDT':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionAUSDT)
def transaccionAUSDT(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('E',34))
    try:
        usuarios=Cargar(cid)
        print(cid)
        if int(usuarios) == cid:
         entrada = float(entrada)
         total=(float(entrada)*tasas)
         print(total)
         tasa.append(tasas)
         clientes.append(-total)
         destino.append('USDT')
         origen.append('ARGENTINA')
         letra.append('I')
         envio.append(float(entrada))
         pedidos.append(m.from_user.id)
         nombre[cid]=entrada
         destinos[cid]="USDT"
         envios[cid]="ARGENTINA"
         tasastwo[cid]=tasas
         letrastwo[cid]="I"
         entradastwo[cid]=total
         Guardartxt()
         bot.send_message(cid,"La tasa de cambio para USDT  es de "+ str(tasas) +" USDT por peso argentino, usted recibira un total de:"+ str(total) +" USDT, pulse el comando /Procesar o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionAUSDT)
@bot.message_handler(commands=['ARGENTINA_VENEZUELA'])
def cantidadAVES(message):
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/ARGENTINA_VENEZUELA':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionAVES)
def transaccionAVES(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('E',24))
    try:
        usuarios=Cargar(cid)
        print(cid)
        if int(usuarios) == cid:
         entrada = float(entrada)
         total=(float(entrada)*tasas)
         clientes.append(-total)
         tasa.append(tasas)
         destino.append('VENEZUELA')
         origen.append('ARGENTINA')
         letra.append('I')
         envio.append(float(entrada))
         pedidos.append(m.from_user.id)
         nombre[cid]=entrada
         destinos[cid]="VENEZUELA"
         envios[cid]="ARGENTINA"
         tasastwo[cid]=tasas
         letrastwo[cid]="I"
         entradastwo[cid]=total
         Guardartxt()
         msg = bot.send_message(cid, "La tasa de cambio para Venezuela  es de   "+ str(tasas) +"   Bolivares por peso argentino, usted recibira un total de: "+ str(total) +" bs pulse el comando /Procesar o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionAVES)
#region envio desde brasil

@bot.message_handler(commands=['BRASIL_ARGENTINA'])
def cantidadBA(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/BRASIL_ARGENTINA':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionBA)
def transaccionBA(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('I',8))
    try:
        usuarios=Cargar(cid)
        print(cid)
        if int(usuarios) == cid:
         entrada = float(entrada)
         total=(float(entrada)*tasas)
         clientes.append(-total)
         tasa.append(tasas)
         destino.append('ARGENTINA')
         origen.append('BRASIL')
         letra.append('H')
         envio.append(float(entrada))
         pedidos.append(m.from_user.id)
         nombre[cid]=entrada
         destinos[cid]="ARGENTINA"
         envios[cid]="BRASIL"
         tasastwo[cid]=tasas
         letrastwo[cid]="H"
         entradastwo[cid]=total
         Guardartxt()
         bot.send_message(cid,"La tasa de cambio para Argentina  es de  "+ str(tasas) +" pesos argentinos por reais, usted recibira un total de:"+ str(total) +" , pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionBA)
@bot.message_handler(commands=['BRASIL_CHILE'])
def cantidadBC(message):
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/BRASIL_CHILE':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionBC)
def transaccionBC(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('I',10))
    try:
        usuarios=Cargar(cid)
        print(cid)
        if int(usuarios) == cid:
         entrada = float(entrada)
         total=(float(entrada)*tasas)
         tasa.append(tasas)
         print(total)
         destino.append('CHILE')
         origen.append('BRASIL')
         letra.append('H')
         clientes.append(-total)
         envio.append(float(entrada))
         pedidos.append(m.from_user.id)
         nombre[cid]=entrada
         destinos[cid]="CHILE"
         envios[cid]="BRASIL"
         tasastwo[cid]=tasas
         letrastwo[cid]="H"
         entradastwo[cid]=total
         Guardartxt()
         bot.send_message(cid,"La tasa de cambio para Chile  es de "+ str(tasas) +" peso chileno por reais, usted recibira un total de:"+ str(total) +" , pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionBC)
@bot.message_handler(commands=['BRASIL_ESPANA'])
def cantidadBES(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/BRASIL_ESPANA':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionBES)
def transaccionBES(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('I',18))
    try:
        usuarios=Cargar(cid)
        print(cid)
        if int(usuarios) == cid:
         entrada = float(entrada)
         total=(float(entrada)*tasas)
         tasa.append(tasas)
         print(total)
         clientes.append(-total)
         destino.append('ESPAÑA')
         origen.append('BRASIL')
         letra.append('H')
         envio.append(float(entrada))
         pedidos.append(m.from_user.id)
         nombre[cid]=entrada
         destinos[cid]="ESPAÑA"
         envios[cid]="BRASIL"
         tasastwo[cid]=tasas
         letrastwo[cid]="H"
         entradastwo[cid]=total
         Guardartxt()
         bot.send_message(cid,"La tasa de cambio para España  es de  "+ str(tasas) +"  Euro por Reais, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionBES)
@bot.message_handler(commands=['BRASIL_EEUU'])
def cantidadBEU(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/BRASIL_EEUU':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionBEU)
def transaccionBEU(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('I',14))
    try:
        usuarios=Cargar(cid)
        print(cid)
        if int(usuarios) == cid:
         entrada = float(entrada)
         total=(float(entrada)*tasas)
         tasa.append(tasas)
         print(total)
         clientes.append(-total)
         destino.append('EEUU')
         origen.append('BRASIL')
         letra.append('H')
         envio.append(float(entrada))
         pedidos.append(m.from_user.id)
         nombre[cid]=entrada
         destinos[cid]="EEUU"
         envios[cid]="BRASIL"
         tasastwo[cid]=tasas
         letrastwo[cid]="H"
         entradastwo[cid]=total
         Guardartxt()
         bot.send_message(cid,"La tasa de cambio para EEUU  es de  "+ str(tasas) +" Dolares por Reais, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionBEU)
@bot.message_handler(commands=['BRASIL_USA'])
def cantidadBUS(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/BRASIL_USA':
        jid=bot.send_message(cid,"Hola Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionBUS)
def transaccionBUS(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('I',14))
    try:
        usuarios=Cargar(cid)
        print(cid)
        if int(usuarios) == cid:
         entrada = float(entrada)
         total=(float(entrada)*tasas)
         clientes.append(-total)
         tasa.append(tasas)
         destino.append('USA')
         origen.append('BRASIL')
         letra.append('H')
         envio.append(float(entrada))
         pedidos.append(m.from_user.id)
         nombre[cid]=entrada
         destinos[cid]="USA"
         envios[cid]="BRASIL"
         tasastwo[cid]=tasas
         letrastwo[cid]="H"
         entradastwo[cid]=total
         Guardartxt()
         bot.send_message(cid,"La tasa de cambio para USA  es de  "+ str(tasas) +" Dolares por Reais, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionBUS)
@bot.message_handler(commands=['BRASIL_PANAMA'])
def cantidadBPAN(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/BRASIL_PANAMA':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionBPAN)
def transaccionBPAN(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('I',12))
    try:
        usuarios=Cargar(cid)
        print(cid)
        if int(usuarios) == cid:
         entrada = float(entrada)
         total=(float(entrada)*tasas)
         clientes.append(-total)
         tasa.append(tasas)
         destino.append('PANAMA')
         origen.append('BRASIL')
         letra.append('H')
         envio.append(float(entrada))
         pedidos.append(m.from_user.id)
         nombre[cid]=entrada
         destinos[cid]="PANAMA"
         envios[cid]="BRASIL"
         tasastwo[cid]=tasas
         letrastwo[cid]="H"
         entradastwo[cid]=total
         Guardartxt()
        bot.send_message(cid,"La tasa de cambio para Panama  es de  "+ str(tasas) +" Dolar Panama por Reais, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionBPAN)
@bot.message_handler(commands=['BRASIL_PERU'])
def cantidadBPER(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/BRASIL_PERU':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionBPER)
def transaccionBPER(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('I',6))
    try:
        usuarios=Cargar(cid)
        print(cid)
        if int(usuarios) == cid:
         entrada = float(entrada)
         total=(float(entrada)*tasas)
         clientes.append(-total)
         tasa.append(tasas)
         destino.append('PERU')
         origen.append('BRASIL')
         letra.append('H')
         envio.append(float(entrada))
         pedidos.append(m.from_user.id)
         nombre[cid]=entrada
         destinos[cid]="PERU"
         envios[cid]="BRASIL"
         tasastwo[cid]=tasas
         letrastwo[cid]="H"
         entradastwo[cid]=total
         Guardartxt()
         bot.send_message(cid,"La tasa de cambio para Peru  es de  "+ str(tasas) +" Soles por Reais, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionBPER)
@bot.message_handler(commands=['BRASIL_USDT'])
def cantidadABSDT(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/BRASIL_USDT':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionBUSDT)
def transaccionBUSDT(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('I',16))
    try:
        usuarios=Cargar(cid)
        print(cid)
        if int(usuarios) == cid:
         entrada = float(entrada)
         total=(float(entrada)*tasas)
         tasa.append(tasas)
         destino.append('USDT')
         origen.append('BRASIL')
         letra.append('H')
         envio.append(float(entrada))
         pedidos.append(m.from_user.id)
         clientes.append(-total)
         nombre[cid]=entrada
         destinos[cid]="USDT"
         envios[cid]="BRASIL"
         tasastwo[cid]=tasas
         letrastwo[cid]="H"
         entradastwo[cid]=total
         Guardartxt()
         bot.send_message(cid,"La tasa de cambio para USDT  es de "+ str(tasas) +" USDT por Reais, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionBUSDT)
@bot.message_handler(commands=['BRASIL_VENEZUELA'])
def cantidadBVES(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/BRASIL_VENEZUELA':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionBVES)
def transaccionBVES(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('I',4))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        destino.append('VENEZUELA')
        origen.append('BRASIL')
        letra.append('H')
        tasa.append(tasas)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        clientes.append(-total)
        nombre[cid]=entrada
        destinos[cid]="VENEZUELA"
        envios[cid]="BRASIL"
        tasastwo[cid]=tasas
        letrastwo[cid]="H"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para Venezuela  es de  "+ str(tasas) +" Bolivares por Reais, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionBVES)
#region envio desde CHILE
@bot.message_handler(commands=['CHILE_BRASIL'])
def cantidadCCHI(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/CHILE_BRASIL':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionCCHI)
def transaccionCCHI(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('G',28))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        tasa.append(tasas)
        destino.append('BRASIL')
        origen.append('CHILE')
        letra.append('G')
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        clientes.append(-total)
        nombre[cid]=entrada
        destinos[cid]="BRASIL"
        envios[cid]="CHILE"
        tasastwo[cid]=tasas
        letrastwo[cid]="G"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para Brasil  es de  "+ str(tasas) +" Reais por peso chileno, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionCCHI)
@bot.message_handler(commands=['CHILE_ARGENTINA'])
def cantidadCARG(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/CHILE_ARGENTINA':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionCARG)
def transaccionCARG(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('G',26))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        tasa.append(tasas)
        print(total)
        destino.append('ARGENTINA')
        origen.append('CHILE')
        letra.append('G')
        clientes.append(-total)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="ARGENTINA"
        envios[cid]="CHILE"
        tasastwo[cid]=tasas
        letrastwo[cid]="G"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para Argentina es de  "+ str(tasas) +" Peso argentino por peso chileno, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionCARG)
@bot.message_handler(commands=['CHILE_ESPANA'])
def cantidadCESP(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/CHILE_ESPANA':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionCESP)
def transaccionCESP(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('G',36))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        tasa.append(tasas)
        destino.append('ESPAÑA')
        origen.append('CHILE')
        letra.append('G')
        clientes.append(-total)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="ESPAÑA"
        envios[cid]="CHILE"
        tasastwo[cid]=tasas
        letrastwo[cid]="G"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para España  es de  "+ str(tasas) +" Euros por peso chileno, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionCESP)
@bot.message_handler(commands=['CHILE_EEUU'])
def cantidadCEEUU(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/CHILE_EEUU':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionCEEUU)
def transaccionCEEUU(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('G',32))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        tasa.append(tasas)
        destino.append('EEUU')
        origen.append('CHILE')
        letra.append('G')
        clientes.append(-total)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="EEUU"
        envios[cid]="CHILE"
        tasastwo[cid]=tasas
        letrastwo[cid]="G"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para EEUU es de  "+ str(tasas) +" Dolares por peso Chileno, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionCEEUU)
@bot.message_handler(commands=['CHILE_USA'])
def cantidadCUSA(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/CHILE_USA':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionCUSA)
def transaccionCUSA(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('G',32))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        tasa.append(tasas)
        destino.append('USA')
        origen.append('CHILE')
        letra.append('G')
        clientes.append(-total)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="USA"
        envios[cid]="CHILE"
        tasastwo[cid]=tasas
        letrastwo[cid]="G"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para USA  es de  "+ str(tasas) +" Dolares por peso chileno, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionCUSA)
@bot.message_handler(commands=['CHILE_PANAMA'])
def cantidadCPAN(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/CHILE_PANAMA':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. " ,reply_markup=hideBoard)
        bot.register_next_step_handler( jid, transaccionCPAN)
def transaccionCPAN(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('G',30))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        destino.append('PANAMA')
        origen.append('CHILE')
        letra.append('G')
        tasa.append(tasas)
        clientes.append(-total)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="PANAMA"
        envios[cid]="CHILE"
        tasastwo[cid]=tasas
        letrastwo[cid]="G"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para Panama  es de  "+ str(tasas) +" Dolar Panama por peso chileno, usted recibira un total de:"+ str(total) +" , pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionCPAN)
@bot.message_handler(commands=['CHILE_PERU'])
def cantidadCPER(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/CHILE_PERU':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionCPER)
def transaccionCPER(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('G',24))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        clientes.append(-total)
        tasa.append(tasas)
        destino.append('PERU')
        origen.append('CHILE')
        letra.append('G')
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="PERU"
        envios[cid]="CHILE"
        tasastwo[cid]=tasas
        letrastwo[cid]="G"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para Peru es de  "+ str(tasas) +" Soles por peso chileno, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionCPER)
@bot.message_handler(commands=['CHILE_USDT'])
def cantidadCUSDT(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/CHILE_USDT':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionCUSDT)
def transaccionCUSDT(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('G',34))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        tasa.append(tasas)
        destino.append('USDT')
        origen.append('CHILE')
        letra.append('G')
        clientes.append(-total)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="USDT"
        envios[cid]="CHILE"
        tasastwo[cid]=tasas
        letrastwo[cid]="G"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para USDT  es de "+ str(tasas) +" Dolares por peso chileno, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionCUSDT)
@bot.message_handler(commands=['CHILE_VENEZUELA'])
def cantidadCVEN(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/CHILE_VENEZUELA':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionCVEN)
def transaccionCVEN(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('G',22))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        tasa.append(tasas)
        destino.append('VENEZUELA')
        origen.append('CHILE')
        letra.append('G')
        clientes.append(-total)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="VENEZUELA"
        envios[cid]="CHILE"
        tasastwo[cid]=tasas
        letrastwo[cid]="G"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para Venezuela  es de  "+ str(tasas) +" Bolivares por peso chileno, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionCVEN)
#REGION ENVIO DESDE ESPAÑA
@bot.message_handler(commands=['ESPANA_BRASIL'])
def cantidadESPB(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/ESPANA_BRASIL':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionESPB)
def transaccionESPB(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('M',12))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        tasa.append(tasas)
        destino.append('BRASIL')
        origen.append('ESPAÑA')
        letra.append('K')
        clientes.append(-total)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="BRASIL"
        envios[cid]="ESPAÑA"
        tasastwo[cid]=tasas
        letrastwo[cid]="K"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para Brasil  es de  "+ str(tasas) +" Reais por euro, usted recibira un total de:"+ str(total) +" , pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionESPB)
@bot.message_handler(commands=['ESPANA_ARGENTINA'])
def cantidadESPA(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/ESPANA_ARGENTINA':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionESPA)
def transaccionESPA(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('M',8))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        tasa.append(tasas)
        destino.append('ARGENTINA')
        origen.append('ESPAÑA')
        letra.append('K')
        clientes.append(-total)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="ARGENTINA"
        envios[cid]="ESPAÑA"
        tasastwo[cid]=tasas
        letrastwo[cid]="K"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para Argentina  es de  "+ str(tasas) +" Peso argentino por euro, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionESPA)
@bot.message_handler(commands=['ESPANA_CHILE'])
def cantidadESPCHI(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/ESPANA_CHILE':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionESPCHI)
def transaccionESPCHI(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('M',10))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        tasa.append(tasas)
        destino.append('CHILE')
        origen.append('ESPAÑA')
        letra.append('K')
        clientes.append(-total)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="CHILE"
        envios[cid]="ESPAÑA"
        tasastwo[cid]=tasas
        letrastwo[cid]="K"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para Chile  es de  "+ str(tasas) +" Peso Chileno por euro, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionESPCHI)
@bot.message_handler(commands=['ESPANA_EEUU'])
def cantidadESPEEUU(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/ESPANA_EEUU':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionESPEEUU)
def transaccionESPEEUU(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('M',14))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        destino.append('EEUU')
        origen.append('ESPAÑA')
        letra.append('K')
        tasa.append(tasas)
        clientes.append(-total)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="EEUU"
        envios[cid]="ESPAÑA"
        tasastwo[cid]=tasas
        letrastwo[cid]="K"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para EEUU  es de  "+ str(tasas) +" Dolares por euro, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionESPEEUU)
@bot.message_handler(commands=['ESPANA_USA'])
def cantidadESPUSA(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/ESPANA_USA':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionESPUSA)
def transaccionESPUSA(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('M',14))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        destino.append('USA')
        origen.append('ESPAÑA')
        letra.append('K')
        tasa.append(tasas)
        clientes.append(-total)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="USA"
        envios[cid]="ESPAÑA"
        tasastwo[cid]=tasas
        letrastwo[cid]="K"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para USA  es de  "+ str(tasas) +" Dolares por euro, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionESPUSA)
@bot.message_handler(commands=['ESPANA_PANAMA'])
def cantidadESPPAN(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/ESPANA_PANAMA':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionESPPAN)
def transaccionESPPAN(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('M',18))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        tasa.append(tasas)
        destino.append('PANAMA')
        origen.append('ESPAÑA')
        letra.append('K')
        clientes.append(-total)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="PANAMA"
        envios[cid]="ESPAÑA"
        tasastwo[cid]=tasas
        letrastwo[cid]="K"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para Panama  es de  "+ str(tasas) +" Dolar Panama por euro, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionESPPAN)
@bot.message_handler(commands=['ESPANA_PERU'])
def cantidadESPPER(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/ESPANA_PERU':
        jid=bot.send_message(cid,"Hola, Por favor Introduzca la cantidad a enviar . ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionESPPER)
def transaccionESPPER(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('M',6))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        tasa.append(tasas)
        destino.append('PERU')
        origen.append('ESPAÑA')
        letra.append('K')
        clientes.append(-total)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="PERU"
        envios[cid]="ESPAÑA"
        tasastwo[cid]=tasas
        letrastwo[cid]="K"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para Peru  es de  "+ str(tasas) +" soles por euro, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionESPPER)
@bot.message_handler(commands=['ESPANA_USDT'])
def cantidadESPUSDT(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/ESPANA_USDT':
        jid=bot.send_message(cid,"Hola,Por favor Introduzca la cantidad a enviar . ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionESPUSDT)
def transaccionESPUSDT(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('M',16))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        tasa.append(tasas)
        destino.append('USDT')
        origen.append('ESPAÑA')
        letra.append('K')
        clientes.append(-total)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="USDT"
        envios[cid]="ESPAÑA"
        tasastwo[cid]=tasas
        letrastwo[cid]="K"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para Usdt  es de  "+ str(tasas) +" euros por Usdt, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionESPUSDT)
@bot.message_handler(commands=['ESPANA_VENEZUELA'])
def cantidadESPVEN(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/ESPANA_VENEZUELA':
        jid=bot.send_message(cid,"Hola, Por favor Introduzca la cantidad a enviar . ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionESPVEN)
def transaccionESPVEN(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('M',4))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        tasa.append(tasas)
        destino.append('VENEZUELA')
        origen.append('ESPAÑA')
        letra.append('K')
        clientes.append(-total)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="VENEZUELA"
        envios[cid]="ESPAÑA"
        tasastwo[cid]=tasas
        letrastwo[cid]="K"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para venezuela  es de  "+ str(tasas) +" bolivar por euro, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionESPVEN)
#REGION ENVIO DESDE EEUU
@bot.message_handler(commands=['EEUU_BRASIL'])
def cantidadEEUUBR(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/EEUU_BRASIL':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionEEUUBR)
def transaccionEEUUBR(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('I',28))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        tasa.append(tasas)
        destino.append('BRASIL')
        origen.append('EEUU')
        letra.append('L')
        clientes.append(-total)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="BRASIL"
        envios[cid]="EEUU"
        tasastwo[cid]=tasas
        letrastwo[cid]="L"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para Brasil  es de "+ str(tasas) +" Reais por dolar, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionEEUUBR)
@bot.message_handler(commands=['EEUU_ARGENTINA'])
def cantidadEEUUAR(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/EEUU_ARGENTINA':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionEEUUAR)
def transaccionEEUUAR(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('I',26))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        clientes.append(-total)
        destino.append('ARGENTINA')
        origen.append('EEUU')
        letra.append('L')
        tasa.append(tasas)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="ARGENTINA"
        envios[cid]="EEUU"
        tasastwo[cid]=tasas
        letrastwo[cid]="L"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para Argentina  es de  "+ str(tasas) +" Peso argentino por dolar, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionEEUUAR)
@bot.message_handler(commands=['EEUU_CHILE'])
def cantidadEEUUCH(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/EEUU_CHILE':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionEEUUCH)
def transaccionEEUUCH(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('I',32))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        destino.append('CHILE')
        origen.append('EEUU')
        letra.append('L')
        tasa.append(tasas)
        clientes.append(-total)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="CHILE"
        envios[cid]="EEUU"
        tasastwo[cid]=tasas
        letrastwo[cid]="L"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para Chile  es de  "+ str(tasas) +" Peso chileno por dolar, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionEEUUCH)
@bot.message_handler(commands=['EEUU_ESPAÑA'])
def cantidadEEUUESP(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/EEUU_ESPAÑA':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionEEUUESP)
def transaccionEEUUESP(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('I',36))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        destino.append('ESPAÑA')
        origen.append('EEUU')
        letra.append('L')
        tasa.append(tasas)
        clientes.append(-total)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="ESPAÑA"
        envios[cid]="EEUU"
        tasastwo[cid]=tasas
        letrastwo[cid]="L"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para España  es de  "+ str(tasas) +" Euro por dolar, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionEEUUESP)
@bot.message_handler(commands=['EEUU_USA'])
def cantidadEEUUBR(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/EEUU_USA':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionEEUUUSA)
def transaccionEEUUUSA(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=1
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*1)
        print(total)
        tasa.append(tasas)
        destino.append('USA')
        origen.append('EEUU')
        letra.append('L')
        clientes.append(-total)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="USA"
        envios[cid]="EEUU"
        tasastwo[cid]=tasas
        letrastwo[cid]="L"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para USA  es de 1 dolar por dolar, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionEEUUUSA)
@bot.message_handler(commands=['EEUU_PANAMA'])
def cantidadEEUUPAN(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/EEUU_PANAMA':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionEEUUPAN)
def transaccionEEUUPAN(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('I',30))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
         entrada = float(entrada)
         total=(float(entrada)*tasas)
         print(total)
         destino.append('PANAMA')
         origen.append('EEUU')
         letra.append('L')
         tasa.append(tasas)
         clientes.append(-total)
         envio.append(float(entrada))
         pedidos.append(m.from_user.id)
         nombre[cid]=entrada
         destinos[cid]="PANAMA"
         envios[cid]="EEUU"
         tasastwo[cid]=tasas
         letrastwo[cid]="L"
         entradastwo[cid]=total
         Guardartxt()
         bot.send_message(cid,"La tasa de cambio para Panama  es de  "+ str(tasas) +" Dolar Panama por dolar, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionEEUUUSA)
@bot.message_handler(commands=['EEUU_PERU'])
def cantidadEEUUPER(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/EEUU_PERU':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionEEUUPER)
def transaccionEEUUPER(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('I',24))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        tasa.append(tasas)
        destino.append('PERU')
        origen.append('EEUU')
        letra.append('L')
        clientes.append(-total)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="PERU"
        envios[cid]="EEUU"
        tasastwo[cid]=tasas
        letrastwo[cid]="L"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para Peru  es de  "+ str(tasas) +" Soles por dolar, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionEEUUPER)
@bot.message_handler(commands=['EEUU_USDT'])
def cantidadEEUUUSDT(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/EEUU_USDT':
        jid=bot.send_message(cid,"Hola, Por favor Introduzca la cantidad a enviar . ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionEEUUUSDT)
def transaccionEEUUUSDT(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('I',34))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        tasa.append(tasas)
        destino.append('USDT')
        origen.append('EEUU')
        letra.append('L')
        clientes.append(-total)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="USDT"
        envios[cid]="EEUU"
        tasastwo[cid]=tasas
        letrastwo[cid]="L"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para USDT  es de "+ str(tasas) +" usdt por dolar, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionEEUUUSDT)
@bot.message_handler(commands=['EEUU_VENEZUELA'])
def cantidadEEUUVEN(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/EEUU_VENEZUELA':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionEEUUVEN)
def transaccionEEUUVEN(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('I',22))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
         entrada = float(entrada)
         total=(float(entrada)*tasas)
         print(total)
         clientes.append(-total)
         destino.append('VENEZUELA')
         origen.append('EEUU')
         letra.append('L')
         tasa.append(tasas)
         envio.append(float(entrada))
         pedidos.append(m.from_user.id)
         nombre[cid]=entrada
         destinos[cid]="VENEZUELA"
         envios[cid]="EEUU"
         tasastwo[cid]=tasas
         letrastwo[cid]="L"
         entradastwo[cid]=total
         Guardartxt()
         bot.send_message(cid,"La tasa de cambio para Venezuela  es de  "+ str(tasas) +" Bolivares por dolar, usted recibira un total de:"+ str(total) +" , pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionEEUUVEN)
#REGION ENVIO DESDE USA
@bot.message_handler(commands=['USA_BRASIL'])
def cantidadUSABR(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/USA_BRASIL':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionUSABR)
def transaccionUSABR(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('I',28))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        tasa.append(tasas)
        destino.append('BRASIL')
        origen.append('USA')
        letra.append('M')
        clientes.append(-total)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="BRASIL"
        envios[cid]="USA"
        tasastwo[cid]=tasas
        letrastwo[cid]="M"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para Brasil  es de  "+ str(tasas) +" Reais por dolar, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionUSABR)
@bot.message_handler(commands=['USA_ARGENTINA'])
def cantidadUSAAR(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/USA_ARGENTINA':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionUSAAR)
def transaccionUSAAR(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('I',26))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        destino.append('ARGENTINA')
        origen.append('USA')
        letra.append('M')
        tasa.append(tasas)
        clientes.append(-total)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="ARGENTINA"
        envios[cid]="USA"
        tasastwo[cid]=tasas
        letrastwo[cid]="M"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para Argentina  es de  "+ str(tasas) +" Pesos argentinos por dolar, usted recibira un total de:"+ str(total) +" , pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionUSAAR)
@bot.message_handler(commands=['USA_CHILE'])
def cantidadUSACHI(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/USA_CHILE':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionUSACHI)
def transaccionUSACHI(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('I',32))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        destino.append('CHILE')
        origen.append('USA')
        letra.append('M')
        tasa.append(tasas)
        clientes.append(-total)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="CHILE"
        envios[cid]="USA"
        tasastwo[cid]=tasas
        letrastwo[cid]="M"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para Chile  es de  "+ str(tasas) +" Pesos chilenos por dolar, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionUSACHI)
@bot.message_handler(commands=['USA_ESPAÑA'])
def cantidadUSAESP(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/USA_ESPAÑA':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionUSAESP)
def transaccionUSAESP(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('I',36))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
         entrada = float(entrada)
         total=(float(entrada)*tasas)
         print(total)
         tasa.append(tasas)
         destino.append('ESPAÑA')
         origen.append('USA')
         letra.append('M')
         clientes.append(-total)
         envio.append(float(entrada))
         pedidos.append(m.from_user.id)
         nombre[cid]=entrada
         destinos[cid]="ESPAÑA"
         envios[cid]="USA"
         tasastwo[cid]=tasas
         letrastwo[cid]="M"
         entradastwo[cid]=total
         Guardartxt()
         bot.send_message(cid,"La tasa de cambio para España  es de  "+ str(tasas) +" Euros por peso dolar, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionUSAESP)
@bot.message_handler(commands=['USA_EEUU'])
def cantidadUSAEEUU(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/USA_EEUU':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionUSAEEUU)
def transaccionUSAEEUU(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=1.00
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*1.00)
        print(total)
        tasa.append(tasas)
        destino.append('EEUU')
        origen.append('USA')
        letra.append('M')
        clientes.append(-total)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="EEUU"
        envios[cid]="USA"
        tasastwo[cid]=tasas
        letrastwo[cid]="M"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para EEUU  es de 1.00 dolar por peso dolar, usted recibira un total de:"+ str(total) +" , pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionUSAEEUU)
@bot.message_handler(commands=['USA_PANAMA'])
def cantidadUSAPAN(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/USA_PANAMA':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionUSAPAN)
def transaccionUSAPAN(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('I',30))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
         entrada = float(entrada)
         total=(float(entrada)*tasas)
         print(total)
         clientes.append(-total)
         tasa.append(tasas)
         destino.append('PANAMA')
         origen.append('USA')
         letra.append('M')
         envio.append(float(entrada))
         pedidos.append(m.from_user.id)
         nombre[cid]=entrada
         destinos[cid]="PANAMA"
         envios[cid]="USA"
         tasastwo[cid]=tasas
         letrastwo[cid]="M"
         entradastwo[cid]=total
         Guardartxt()
         bot.send_message(cid,"La tasa de cambio para Panama  es de  "+ str(tasas) +" Dolar Panama por peso dolar, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionUSAPAN)
@bot.message_handler(commands=['USA_PERU'])
def cantidadUSAPERU(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/USA_PERU':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionUSAPERU)
def transaccionUSAPERU(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('I',24))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        destino.append('PERU')
        origen.append('USA')
        letra.append('M')
        clientes.append(-total)
        tasa.append(tasas)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="PERU"
        envios[cid]="USA"
        tasastwo[cid]=tasas
        letrastwo[cid]="M"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para Peru  es de  "+ str(tasas) +" Soles por dolar, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionUSAPERU)
@bot.message_handler(commands=['USA_USDT'])
def cantidadUSAUSDT(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/USA_USDT':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionUSAUSDT)
def transaccionUSAUSDT(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('I',34))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        destino.append('USDT')
        origen.append('USA')
        letra.append('M')
        clientes.append(-total)
        tasa.append(tasas)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="USDT"
        envios[cid]="USA"
        tasastwo[cid]=tasas
        letrastwo[cid]="M"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para USDT  es de "+ str(tasas) +" usdt por peso dolar, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionUSAUSDT)
@bot.message_handler(commands=['USA_VENEZUELA'])
def cantidadUSAVENEZUELA(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/USA_VENEZUELA':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionUSAVENEZUELA)
def transaccionUSAVENEZUELA(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('I',22))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        destino.append('VENEZUELA')
        origen.append('USA')
        letra.append('M')
        clientes.append(-total)
        tasa.append(tasas)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="VENEZUELA"
        envios[cid]="USA"
        tasastwo[cid]=tasas
        letrastwo[cid]="M"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para Venezuela  es de  "+ str(tasas) +" Bolivares por dolar, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionUSAVENEZUELA)
#REGION ENVIO DESDE PANAMA
@bot.message_handler(commands=['PANAMA_BRASIL'])
def cantidadPANBR(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/PANAMA_BRASIL':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionPANBR)
def transaccionPANBR(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('K',12))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        destino.append('BRASIL')
        origen.append('PANAMA')
        letra.append('J')
        clientes.append(-total)
        tasa.append(tasas)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="BRASIL"
        envios[cid]="PANAMA"
        tasastwo[cid]=tasas
        letrastwo[cid]="J"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para Brasil  es de  "+ str(tasas) +" Reais por Dolar Panama, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionPANBR)
@bot.message_handler(commands=['PANAMA_ARGENTINA'])
def cantidadPANARG(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/PANAMA_ARGENTINA':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionPANARG)
def transaccionPANARG(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('K',8))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        destino.append('ARGENTINA')
        origen.append('PANAMA')
        letra.append('J')
        clientes.append(-total)
        tasa.append(tasas)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="ARGENTINA"
        envios[cid]="PANAMA"
        tasastwo[cid]=tasas
        letrastwo[cid]="J"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para Argentina  es de  "+ str(tasas) +" Peso argentino por Dolar Panama, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionPANARG)
@bot.message_handler(commands=['PANAMA_CHILE'])
def cantidadPANCHI(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/PANAMA_CHILE':
        jid=bot.send_message(cid,"Hola, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionPANCHI)
def transaccionPANCHI(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('K',10))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        destino.append('CHILE')
        origen.append('PANAMA')
        letra.append('J')
        clientes.append(-total)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="CHILE"
        envios[cid]="PANAMA"
        tasastwo[cid]=tasas
        letrastwo[cid]="J"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para Chile  es de  "+ str(tasas) +" Peso chileno por Dolar Panama, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionPANCHI)
@bot.message_handler(commands=['PANAMA_ESPAÑA'])
def cantidadPANESP(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/PANAMA_ESPAÑA':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionPANESP)
def transaccionPANESP(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('K',18))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        clientes.append(-total)
        tasa.append(tasas)
        destino.append('ESPAÑA')
        origen.append('PANAMA')
        letra.append('J')
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="ESPAÑA"
        envios[cid]="PANAMA"
        tasastwo[cid]=tasas
        letrastwo[cid]="J"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para España  es de  "+ str(tasas) +" Euro por Dolar Panama, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionPANESP)
@bot.message_handler(commands=['PANAMA_EEUU'])
def cantidadPANEEUU(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/PANAMA_EEUU':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionPANEEUU)
def transaccionPANEEUU(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('K',14))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        clientes.append(-total)
        tasa.append(tasas)
        destino.append('EEUU')
        origen.append('PANAMA')
        letra.append('J')
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="EEUU"
        envios[cid]="PANAMA"
        tasastwo[cid]=tasas
        letrastwo[cid]="J"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para EEUU  es de  "+ str(tasas) +" Dolar por Dolar Panama, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionPANEEUU)
@bot.message_handler(commands=['PANAMA_USA'])
def cantidadPANUSA(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/PANAMA_USA':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionPANUSA)
def transaccionPANUSA(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('K',14))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        destino.append('USA')
        origen.append('PANAMA')
        letra.append('J')
        tasa.append(tasas)
        clientes.append(-total)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="USA"
        envios[cid]="PANAMA"
        tasastwo[cid]=tasas
        letrastwo[cid]="J"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para USA  es de  "+ str(tasas) +" Dolar por Dolar Panama, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionPANUSA)
@bot.message_handler(commands=['PANAMA_PERU'])
def cantidadPANPER(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/PANAMA_PERU':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionPANPER)
def transaccionPANPER(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('K',6))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        destino.append('PERU')
        origen.append('PANAMA')
        letra.append('J')
        tasa.append(tasas)
        clientes.append(-total)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="PERU"
        envios[cid]="PANAMA"
        tasastwo[cid]=tasas
        letrastwo[cid]="J"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para Peru  es de  "+ str(tasas) +" Soles por Dolar Panama, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionPANPER)
@bot.message_handler(commands=['PANAMA_USDT'])
def cantidadPANUSDT(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/PANAMA_USDT':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionPANUSDT)
def transaccionPANUSDT(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('K',16))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        destino.append('USDT')
        origen.append('PANAMA')
        letra.append('J')
        tasa.append(tasas)
        clientes.append(-total)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="USDT"
        envios[cid]="PANAMA"
        tasastwo[cid]=tasas
        letrastwo[cid]="J"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para USDT  es de "+ str(tasas) +" usdt por Dolar Panama, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionPANUSDT)
@bot.message_handler(commands=['PANAMA_VENEZUELA'])
def cantidadPANVEN(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/PANAMA_VENEZUELA':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionPANVEN)
def transaccionPANVEN(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('K',4))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        destino.append('VENEZUELA')
        origen.append('PANAMA')
        letra.append('J')
        tasa.append(tasas)
        clientes.append(-total)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="VENEZUELA"
        envios[cid]="PANAMA"
        tasastwo[cid]=tasas
        letrastwo[cid]="J"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para Venezuela  es de  "+ str(tasas) +" Bolivares por Dolar Panama, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionPANVEN)
#REGION ENVIO PERU
@bot.message_handler(commands=['PERU_ARGENTINA'])
def cantidadPERUARG(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/PERU_ARGENTINA':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionPERUARG)
def transaccionPERUARG(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('G',6))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        tasa.append(tasas)
        destino.append('ARGENTINA')
        origen.append('PERU')
        letra.append('F')
        clientes.append(-total)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="ARGENTINA"
        envios[cid]="PERU"
        tasastwo[cid]=tasas
        letrastwo[cid]="F"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para Argentina  es de  "+ str(tasas) +" Peso argentino por sol, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionPERUARG)
@bot.message_handler(commands=['PERU_BRASIL'])
def cantidadPERUBR(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/PERU_BRASIL':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionPERUBR)
def transaccionPERUBR(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('G',10))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        destino.append('BRASIL')
        origen.append('PERU')
        letra.append('F')
        tasa.append(tasas)
        clientes.append(-total)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="BRASIL"
        envios[cid]="PERU"
        tasastwo[cid]=tasas
        letrastwo[cid]="F"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para Brasil  es de  "+ str(tasas) +" Reais por sol, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionPERUBR)
@bot.message_handler(commands=['PERU_CHILE'])
def cantidadPERUCHI(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/PERU_CHILE':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionPERUCHI)
def transaccionPERUCHI(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('G',9))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        destino.append('CHILE')
        origen.append('PERU')
        letra.append('F')
        clientes.append(-total)
        tasa.append(tasas)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="CHILE"
        envios[cid]="PERU"
        tasastwo[cid]=tasas
        letrastwo[cid]="F"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para Chile  es de  "+ str(tasas) +" Peso chileno por sol, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionPERUCHI)
@bot.message_handler(commands=['PERU_ESPANA'])
def cantidadPERUESP(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/PERU_ESPANA':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionPERUESP)
def transaccionPERUESP(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('G',18))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        destino.append('ESPAÑA')
        origen.append('PERU')
        letra.append('F')
        tasa.append(tasas)
        clientes.append(-total)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="ESPAÑA"
        envios[cid]="PERU"
        tasastwo[cid]=tasas
        letrastwo[cid]="F"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para Espana  es de  "+ str(tasas) +" Euro por sol, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionPERUESP)
@bot.message_handler(commands=['PERU_EEUU'])
def cantidadPERUEEUU(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/PERU_EEUU':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionPERUEEUU)
def transaccionPERUEEUU(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('G',14))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        destino.append('EEUU')
        origen.append('PERU')
        letra.append('F')
        tasa.append(tasas)
        clientes.append(-total)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="EEUU"
        envios[cid]="PERU"
        tasastwo[cid]=tasas
        letrastwo[cid]="F"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para EEUU  es de  "+ str(tasas) +" Dolares por sol, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionPERUEEUU)
@bot.message_handler(commands=['PERU_USA'])
def cantidadPERUSA(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/PERU_USA':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionPERUSA)
def transaccionPERUSA(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('G',14))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        destino.append('USA')
        origen.append('PERU')
        letra.append('F')
        tasa.append(tasas)
        clientes.append(-total)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="USA"
        envios[cid]="PERU"
        tasastwo[cid]=tasas
        letrastwo[cid]="F"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para USA  es de  "+ str(tasas) +" Dolares por sol, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionPERUSA)
@bot.message_handler(commands=['PERU_PANAMA'])
def cantidadPERUPANAMA(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/PERU_PANAMA':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionPERUPANAMA)
def transaccionPERUPANAMA(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('G',12))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        destino.append('PANAMA')
        origen.append('PERU')
        letra.append('F')
        clientes.append(-total)
        tasa.append(tasas)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="PANAMA"
        envios[cid]="PERU"
        tasastwo[cid]=tasas
        letrastwo[cid]="F"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para Panama  es de  "+ str(tasas) +" Dolar Panama por sol, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionPERUPANAMA)
@bot.message_handler(commands=['PERU_USDT'])
def cantidadPERUUSDT(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/PERU_USDT':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionPERUUSDT)
def transaccionPERUUSDT(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('G',16))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        destino.append('USDT')
        origen.append('PERU')
        letra.append('F')
        tasa.append(tasas)
        clientes.append(-total)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="USDT"
        envios[cid]="PERU"
        tasastwo[cid]=tasas
        letrastwo[cid]="F"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para USDT  es de "+ str(tasas) +" Dolar usdt por sol, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionPERUUSDT)
@bot.message_handler(commands=['PERU_VENEZUELA'])
def cantidadPERUVEN(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/PERU_VENEZUELA':
        jid=bot.send_message(cid,"Hola, Por favor introduzca la cantidad a enviar. ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionPERUVEN)
def transaccionPERUVEN(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('G',4))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        destino.append('VENEZUELA')
        origen.append('PERU')
        letra.append('F')
        tasa.append(tasas)
        clientes.append(-total)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="VENEZUELA"
        envios[cid]="PERU"
        tasastwo[cid]=tasas
        letrastwo[cid]="F"
        entradastwo[cid]=total
        Guardartxt()
        bot.send_message(cid,"La tasa de cambio para Venezuela  es de  "+ str(tasas) +" Bolivares por sol, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionPERUVEN)
# Region USDT ENVIO
@bot.message_handler(commands=['USDT_BRASIL'])
def cantidadUSDTBR(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/USDT_BRASIL':
        jid=bot.send_message(cid,"Hola, Por favor Introduzca la cantidad a enviar . ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionUSDTBR)



def transaccionUSDTBR(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('K',28))

    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        clientes.append(-total)
        destino.append('BRASIL')
        origen.append('USDT')
        letra.append('N')
        tasa.append(tasas)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="BRASIL"
        envios[cid]="USDT"
        tasastwo[cid]=tasas
        letrastwo[cid]="N"
        entradastwo[cid]=total
        Guardartxt()
        sid=bot.send_message(cid,"La tasa de cambio para Brasil es de "+ str(tasas) +" reais por dolar Usdt, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")

    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionUSDTBR)
@bot.message_handler(commands=['USDT_ARGENTINA'])
def cantidadUSDTAR(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/USDT_ARGENTINA':
        jid=bot.send_message(cid,"Hola, Por favor Introduzca la cantidad a enviar . ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionUSDTAR)

def transaccionUSDTAR(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('K',26))

    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        clientes.append(-total)
        destino.append('ARGENTINA')
        origen.append('USDT')
        letra.append('N')
        tasa.append(tasas)
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="ARGENTINA"
        envios[cid]="USDT"
        tasastwo[cid]=tasas
        letrastwo[cid]="N"
        entradastwo[cid]=total
        Guardartxt()
        envio.append(float(entrada))
        sid=bot.send_message(cid,"La tasa de cambio para Argentina  es de "+ str(tasas) +" Peso argentina por dolar usdt, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar o pulse /cerrar para anular transaccion")

    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionUSDTAR)
@bot.message_handler(commands=['USDT_CHILE'])
def cantidadUSDTCHI(message):
     print('entro')
     nombre=message.text
     cid=message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/USDT_CHILE':
        jid=bot.send_message(cid,"Hola, Por favor Introduzca la cantidad a enviar . ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionUSDTCHI)

def transaccionUSDTCHI(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('K',32))

    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
         entrada = float(entrada)
         total=(float(entrada)*tasas)
         print(total)
         clientes.append(-total)
         tasa.append(tasas)
         destino.append('CHILE')
         origen.append('USDT')
         letra.append('N')
         envio.append(float(entrada))
         pedidos.append(m.from_user.id)
         nombre[cid]=entrada
         destinos[cid]="CHILE"
         envios[cid]="USDT"
         tasastwo[cid]=tasas
         letrastwo[cid]="N"
         entradastwo[cid]=total
         Guardartxt()
         sid=bot.send_message(cid,"La tasa de cambio para CHILE  es de "+ str(tasas) +" USDT por PESO CHILENO, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar o pulse /cerrar para anular transaccion")

    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionUSDTCHI)
@bot.message_handler(commands=['USDT_ESPAÑA'])
def cantidadUSDTESP(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/USDT_ESPAÑA':
        jid=bot.send_message(cid,"Hola,Por favor Introduzca la cantidad a enviar . ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionUSDTESP)

def transaccionUSDTESP(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('K',36))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        tasa.append(tasas)
        clientes.append(-total)
        destino.append('ESPAÑA')
        origen.append('USDT')
        letra.append('N')
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="ESPAÑA"
        envios[cid]="USDT"
        tasastwo[cid]=tasas
        letrastwo[cid]="N"
        entradastwo[cid]=total
        Guardartxt()
        sid=bot.send_message(cid,"La tasa de cambio para españa  es de "+ str(tasas) +" USDT por EURO, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionUSDTESP)
@bot.message_handler(commands=['USDT_EEUU'])
def cantidadUSDTEU(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/USDT_EEUU':
        jid=bot.send_message(cid,"Hola, Por favor Introduzca la cantidad a enviar . ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionUSDTEU)

def transaccionUSDTEU(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('K',34))

    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        tasa.append(tasas)
        clientes.append(-total)
        destino.append('EEUU')
        origen.append('USDT')
        letra.append('N')
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="EEUU"
        envios[cid]="USDT"
        tasastwo[cid]=tasas
        letrastwo[cid]="N"
        entradastwo[cid]=total
        Guardartxt()
        sid=bot.send_message(cid,"La tasa de cambio para EEUU  es de "+ str(tasas) +" Dolares por dolar usdt, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar o pulse /cerrar para anular transaccion")

    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionUSDTEU)
@bot.message_handler(commands=['USDT_USA'])
def cantidadUSDTUSA(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/USDT_USA':
        jid=bot.send_message(cid,"Hola, Por favor Introduzca la cantidad a enviar . ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionUSDTUSA)

def transaccionUSDTUSA(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('K',34))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        tasa.append(tasas)
        clientes.append(-total)
        destino.append('USA')
        origen.append('USDT')
        letra.append('N')
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="USA"
        envios[cid]="USDT"
        tasastwo[cid]=tasas
        letrastwo[cid]="N"
        entradastwo[cid]=total
        Guardartxt()
        sid=bot.send_message(cid,"La tasa de cambio para usa  es de "+ str(tasas) +" Dolares por dolar usdt, usted recibira un total de:"+ str(total) +" , pulse el comando /Procesar o pulse /cerrar para anular transaccion")

    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionUSDTUSA)
@bot.message_handler(commands=['USDT_PANAMA'])
def cantidadUSDTPAN(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/USDT_PANAMA':
        jid=bot.send_message(cid,"Hola, Por favor Introduzca la cantidad a enviar . ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionUSDTPAN)

def transaccionUSDTPAN(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('K',30))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        tasa.append(tasas)
        clientes.append(-total)
        destino.append('PANAMA')
        origen.append('USDT')
        letra.append('N')
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="PANAMA"
        envios[cid]="USDT"
        tasastwo[cid]=tasas
        letrastwo[cid]="N"
        entradastwo[cid]=total
        Guardartxt()
        sid=bot.send_message(cid,"La tasa de cambio para Panama  es de "+ str(tasas) +" USDT por dolar PANAMA, usted recibira un total de:"+ str(total) +" , pulse el comando /Procesar o pulse /cerrar para anular transaccion")

    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionUSDTPAN)
@bot.message_handler(commands=['USDT_PERU'])
def cantidadUSDTPER(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/USDT_PERU':
        jid=bot.send_message(cid,"Hola, Por favor Introduzca la cantidad a enviar . ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionUSDTPER)
def transaccionUSDTPER(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('K',24))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
         entrada = float(entrada)
         total=(float(entrada)*tasas)
         print(total)
         tasa.append(tasas)
         clientes.append(-total)
         destino.append('PERU')
         origen.append('USDT')
         letra.append('N')
         envio.append(float(entrada))
         pedidos.append(m.from_user.id)
         nombre[cid]=entrada
         destinos[cid]="PERU"
         envios[cid]="USDT"
         tasastwo[cid]=tasas
         letrastwo[cid]="N"
         entradastwo[cid]=total
         Guardartxt()
         bot.send_message(cid,"La tasa de cambio para Peru  es de "+ str(tasas) +" SOLES por DOLAR USDT, usted recibira un total de:"+ str(total) +" , pulse el comando /Procesar o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionUSDTPER)
@bot.message_handler(commands=['USDT_VENEZUELA'])
def cantidadUSDTVEN(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/USDT_VENEZUELA':
        jid=bot.send_message(cid,"Hola, Por favor Introduzca la cantidad a enviar . ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionUSDTVEN)
def transaccionUSDTVEN(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('K',22))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
         entrada = float(entrada)
         total=(float(entrada)*tasas)
         print(total)
         tasa.append(tasas)
         clientes.append(-total)
         destino.append('VENEZUELA')
         origen.append('USDT')
         letra.append('N')
         envio.append(float(entrada))
         pedidos.append(m.from_user.id)
         nombre[cid]=entrada
         destinos[cid]="VENEZUELA"
         envios[cid]="USDT"
         tasastwo[cid]=tasas
         letrastwo[cid]="N"
         entradastwo[cid]=total
         Guardartxt()
         bot.send_message(cid,"La tasa de cambio para Venezuela  es de  "+ str(tasas) +"  BOLIVARES por DOLAR USDT, usted recibira un total de:"+ str(total) +" , pulse el comando /Procesar o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionUSDTVEN)
#region envio desde venezuela
@bot.message_handler(commands=['VENEZUELA_BRASIL'])
def cantidadVENBR(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/VENEZUELA_BRASIL':
        jid=bot.send_message(cid,"Hola, Por favor Introduzca la cantidad a enviar . ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionVENBR)



def transaccionVENBR(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('E',10))

    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        clientes.append(-total)
        destino.append('BRASIL')
        origen.append('VENEZUELA')
        letra.append('E')
        tasa.append(tasas)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="BRASIL"
        envios[cid]="VENEZUELA"
        tasastwo[cid]=tasas
        letrastwo[cid]="E"
        entradastwo[cid]=total
        Guardartxt()
        sid=bot.send_message(cid,"La tasa de cambio para Brasil es de  "+ str(tasas) +" reais por cada 1 bolivar, usted recibira un total de:"+ str(total) +" , pulse el comando /Procesar ,para procesar transaccion o pulse /cerrar para anular transaccion")

    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionVENBR)
@bot.message_handler(commands=['VENEZUELA_ARGENTINA'])
def cantidadVENAR(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/VENEZUELA_ARGENTINA':
        jid=bot.send_message(cid,"Hola, Por favor Introduzca la cantidad a enviar . ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionVENAR)

def transaccionVENAR(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('E',6))

    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        clientes.append(-total)
        destino.append('ARGENTINA')
        origen.append('VENEZUELA')
        letra.append('E')
        tasa.append(tasas)
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="ARGENTINA"
        envios[cid]="VENEZUELA"
        tasastwo[cid]=tasas
        letrastwo[cid]="E"
        entradastwo[cid]=total
        Guardartxt()
        sid=bot.send_message(cid,"La tasa de cambio para Argentina  es de  "+ str(tasas) +" Peso argentina por cada bolivar, usted recibira un total de:"+ str(total) +" , pulse el comando /Procesar o pulse /cerrar para anular transaccion")

    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionVENAR)
@bot.message_handler(commands=['VENEZUELA_CHILE'])
def cantidadVENCHI(message):
     print('entro')
     nombre=message.text
     cid=message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/VENEZUELA_CHILE':
        jid=bot.send_message(cid,"Hola, Por favor Introduzca la cantidad a enviar . ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionVENCHI)

def transaccionVENCHI(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('E',8))

    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
         entrada = float(entrada)
         total=(float(entrada)*tasas)
         print(total)
         clientes.append(-total)
         tasa.append(tasas)
         destino.append('CHILE')
         origen.append('VENEZUELA')
         letra.append('E')
         envio.append(float(entrada))
         pedidos.append(m.from_user.id)
         nombre[cid]=entrada
         destinos[cid]="CHILE"
         envios[cid]="VENEZUELA"
         tasastwo[cid]=tasas
         letrastwo[cid]="E"
         entradastwo[cid]=total
         Guardartxt()
         sid=bot.send_message(cid,"La tasa de cambio para CHILE  es de  "+ str(tasas) +" peso chileno por cada bolivar, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar o pulse /cerrar para anular transaccion")

    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionVENCHI)
@bot.message_handler(commands=['VENEZUELA_ESPAÑA'])
def cantidadVENESP(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/VENEZUELA_ESPAÑA':
        jid=bot.send_message(cid,"Hola,Por favor Introduzca la cantidad a enviar . ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionVENESP)

def transaccionVENESP(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('E',18))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        tasa.append(tasas)
        clientes.append(-total)
        destino.append('ESPAÑA')
        origen.append('VENEZUELA')
        letra.append('E')
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="ESPAÑA"
        envios[cid]="VENEZUELA"
        tasastwo[cid]=tasas
        letrastwo[cid]="E"
        entradastwo[cid]=total
        Guardartxt()
        sid=bot.send_message(cid,"La tasa de cambio para españa  es de  "+ str(tasas) +" euros por cada bolivar , usted recibira un total de:"+ str(total) +" , pulse el comando /Procesar o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionVENESP)
@bot.message_handler(commands=['VENEZUELA_EEUU'])
def cantidadVENEU(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/VENEZUELA_EEUU':
        jid=bot.send_message(cid,"Hola, Por favor Introduzca la cantidad a enviar . ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionVENEU)

def transaccionVENEU(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('E',14))

    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        tasa.append(tasas)
        clientes.append(-total)
        destino.append('EEUU')
        origen.append('VENEZUELA')
        letra.append('E')
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="EEUU"
        envios[cid]="VENEZUELA"
        tasastwo[cid]=tasas
        letrastwo[cid]="E"
        entradastwo[cid]=total
        Guardartxt()
        sid=bot.send_message(cid,"La tasa de cambio para EEUU  es de  "+ str(tasas) +" Dolares por cada bolivar, usted recibira un total de:"+ str(total) +" dolares, pulse el comando /Procesar o pulse /cerrar para anular transaccion")

    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionVENEU)
@bot.message_handler(commands=['VENEZUELA_USA'])
def cantidadVENUSA(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/VENEZUELA_USA':
        jid=bot.send_message(cid,"Hola, Por favor Introduzca la cantidad a enviar . ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionUSDTUSA)

def transaccionVENUSA(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('E',10))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        tasa.append(tasas)
        clientes.append(-total)
        destino.append('USA')
        origen.append('VENEZUELA')
        letra.append('E')
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="USA"
        envios[cid]="VENEZUELA"
        tasastwo[cid]=tasas
        letrastwo[cid]="E"
        entradastwo[cid]=total
        Guardartxt()
        sid=bot.send_message(cid,"La tasa de cambio para usa  es de  "+ str(tasas) +" Dolares por cada bolivar, usted recibira un total de:"+ str(total) +" dolares, pulse el comando /Procesar o pulse /cerrar para anular transaccion")

    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionVENUSA)
@bot.message_handler(commands=['VENEZUELA_PANAMA'])
def cantidadVENPAN(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/VENEZUELA_PANAMA':
        jid=bot.send_message(cid,"Hola, Por favor Introduzca la cantidad a enviar . ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionVEPAN)

def transaccionVEPAN(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('E',12))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
        entrada = float(entrada)
        total=(float(entrada)*tasas)
        print(total)
        tasa.append(tasas)
        clientes.append(-total)
        destino.append('PANAMA')
        origen.append('VENEZUELA')
        letra.append('E')
        envio.append(float(entrada))
        pedidos.append(m.from_user.id)
        nombre[cid]=entrada
        destinos[cid]="PANAMA"
        envios[cid]="VENEZUELA"
        tasastwo[cid]=tasas
        letrastwo[cid]="E"
        entradastwo[cid]=total
        Guardartxt()
        sid=bot.send_message(cid,"La tasa de cambio para Panama  es de  "+ str(tasas) +" dolares por cada bolivar, usted recibira un total de:"+ str(total) +" soles, pulse el comando /Procesar o pulse /cerrar para anular transaccion")

    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionVEPAN)
@bot.message_handler(commands=['VENEZUELA_PERU'])
def cantidadVEPER(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/VENEZUELA_PERU':
        jid=bot.send_message(cid,"Hola, Por favor Introduzca la cantidad a enviar . ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionVEPER)
def transaccionVEPER(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('E',4))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
         entrada = float(entrada)
         total=(float(entrada)*tasas)
         print(total)
         tasa.append(tasas)
         clientes.append(-total)
         destino.append('PERU')
         origen.append('VENEZUELA')
         letra.append('E')
         envio.append(float(entrada))
         pedidos.append(m.from_user.id)
         nombre[cid]=entrada
         destinos[cid]="PERU"
         envios[cid]="VENEZUELA"
         tasastwo[cid]=tasas
         letrastwo[cid]="E"
         entradastwo[cid]=total
         Guardartxt()
         bot.send_message(cid,"La tasa de cambio para PERU  es de  "+ str(tasas) +" SOLES por cada bolivar, usted recibira un total de:"+ str(total) +" USDT, pulse el comando /Procesar o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionVEPER)
@bot.message_handler(commands=['VENEZUELA_USDT'])
def cantidadVEUSDT(message):
     print('entro')
     nombre=message.text
     cid = message.from_user.id
     usuarios=Cargar(cid)
     print(cid)
     if int(usuarios) == cid and nombre == '/VENEZUELA_USDT':
        jid=bot.send_message(cid,"Hola, Por favor Introduzca la cantidad a enviar . ",reply_markup=hideBoard )
        bot.register_next_step_handler( jid, transaccionVEUSDT)
def transaccionVEUSDT(m):
    cid = m.from_user.id
    entrada=m.text
    tasas=float(retorna_tasas('E',16))
    try:
       usuarios=Cargar(cid)
       print(cid)
       if int(usuarios) == cid:
         entrada = float(entrada)
         total=(float(entrada)*tasas)
         print(total)
         tasa.append(tasas)
         clientes.append(-total)
         destino.append('USDT')
         origen.append('VENEZUELA')
         letra.append('E')
         envio.append(float(entrada))
         pedidos.append(m.from_user.id)
         nombre[cid]=entrada
         destinos[cid]="USDT"
         envios[cid]="VENEZUELA"
         tasastwo[cid]=tasas
         letrastwo[cid]="E"
         entradastwo[cid]=total
         Guardartxt()
         bot.send_message(cid,"La tasa de cambio para USDT  es de "+ str(tasas) +" USDT por cada bolivar, usted recibira un total de:"+ str(total) +" USDT, pulse el comando /Procesar o pulse /cerrar para anular transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida")
        bot.register_next_step_handler( jid, transaccionVEUSDT)

@bot.message_handler(commands=['admin'])
def admin_reporte(message):
    cid=message.from_user.id
    if os.stat("reporte.json").st_size == 0:
       print("Vacío")
    else :
        print('aqui')
        with open('reporte.json', 'r') as archivo:
             datos = json.load(archivo)
             for client in datos['clientes']:
                 retorna=client['informacion']
                 status=client['status']
                 usuario=client['usuario']

                 bot.send_message(cid,"Reportes:"+retorna+" Usuario:"+usuario+" Status:"+status+"")
def procesar_solicitud(message):
    texto=message.text
    cid = message.from_user.id
    usuarios=Cargar(cid)
    if int(usuarios) == cid and texto == '/Procesar':
       valor=float(transaccion(cid,"entradas"))
       letra=transaccion(cid,"letras")
       orig=transaccion(cid,"envios")
       destino=transaccion(cid,"destinos")
       envia=float(transaccion(cid,"envia"))
       if destino == "BRASIL":
          valores=float(retorna_tasas('C',20))
          exportarsheets((-valor),'H',letra,orig,(valores),envia)
          msg=bot.send_message(cid,"Solicitud Procesada, favor enviar los siguientes datos Brasil:  Chave Pix: ,  Nombre del Titular:")
          bot.register_next_step_handler(msg,capturar_datos)
       elif destino == "ARGENTINA":
          valores=float(retorna_tasas('C',11))
          exportarsheets((-valor),'I',letra,orig,(valores),envia)
          msg=bot.send_message(cid,"Solicitud Procesada, favor enviar los siguientes datos MercadoPago:  CVU: , Nombre del Titular:")
          bot.register_next_step_handler(msg,capturar_datos)
       elif destino == "CHILE":
          valores=float(retorna_tasas('C',14))
          exportarsheets((-valor),'G',letra,orig,(valores),envia)
          msg=bot.send_message(cid,"Solicitud Procesada, favor enviar los siguientes datos  Chile Transferencia Bancaria:  Nombre del banco: , Nro de cuenta:, Rut:, Correo:, Nombre del Titular:")
          bot.register_next_step_handler(msg,capturar_datos)
       elif destino == "ESPAÑA":
          valores=float(retorna_tasas('C',29))
          exportarsheets((-valor),'K',letra,orig,(valores),envia)
          msg=bot.send_message(cid,"Solicitud Procesada, favor enviar los siguientes datos Transferencia Bancaria y Bizum:  Nombre del banco: , Nro de cuenta:, telefono:, Nombre del Titular:")
          bot.register_next_step_handler(msg,capturar_datos)
       elif destino == "EEUU":
          valores=float(retorna_tasas('C',26))
          exportarsheets((-valor),'L',letra,orig,valores,envia)
          msg=bot.send_message(cid,"Solicitud Procesada, favor enviar los siguientes datos ZELLE: Correo electronico:, Nombre del Titular:")
          bot.register_next_step_handler(msg,capturar_datos)
       elif destino == "USA":
          valores=float(retorna_tasas('C',26))
          exportarsheets((-valor),'M',letra[0],orig,valores,envia)
          msg=bot.send_message(cid,"Solicitud Procesada, favor enviar los siguientes  datos ZELLE: Correo electronico:, Nombre del Titular:")
          bot.register_next_step_handler(msg,capturar_datos)
       elif destino == 'PANAMA':
          valores=float(retorna_tasas('C',23))
          exportarsheets((-valor),'J',letra,orig,valores,envia)
          msg=bot.send_message(cid,"Solicitud Procesada, favor enviar los siguientes datos Transferencia Banco general de panama Yappy: Nro de cuenta: Telefono:, Nombre del Titular:")
          bot.register_next_step_handler(msg,capturar_datos)
       elif destino == 'PERU':
          valores=float(retorna_tasas('C',8))
          exportarsheets((-valor),'F',letra,orig,valores,envia)
          msg=bot.send_message(cid,"Solicitud Procesada, favor enviar los siguientes datos Transferencia Bancaria Yape, Plin: Nombre del Banco:, Nro de cuenta:, telefono:, Nombre del Titular:")
          bot.register_next_step_handler(msg,capturar_datos)
       elif destino == 'USDT':
          valores=float(retorna_tasas('C',17))
          exportarsheets((-valor),'N',letra,orig,valores,envia)
          msg=bot.send_message(cid,"Solicitud Procesada, favor enviar los siguientes datos correo o billetera asociado:")
          bot.register_next_step_handler(msg,capturar_datos)
       elif destino == 'VENEZUELA':
          valores=float(retorna_tasas('C',5))
          exportarsheets((-valor),'E',letra,orig,valores,envia)
          msg=bot.send_message(cid,"Solicitud Procesada, favor enviar los siguientes datos Transferencia Bancaria:  Nombre del banco: , Nro de cuenta:, cedula:, telefono:, Nombre del Titular:")
          bot.register_next_step_handler(msg,capturar_datos)
    elif cid > 0  and texto == '/cerrar':
         bot.send_message(cid,"Gracias por visitar nuestra casa de cambio Iberogestion, pulse el comando /start para iniciar proceso")
         destino.clear()
         clientes.clear()
         denominacion.clear()
         origen.clear()
         letra.clear()
         tasa.clear()
         envio.clear()
def capturar_datos(message):
    cid = message.from_user.id
    print(message.text)
    markup = types.ReplyKeyboardMarkup()
    mensaje =  " (@" + str(message.from_user.username) + ")"
    admin="(@IberoGestion)"
    usuarios=Cargar(cid)
    if int(usuarios) == cid:
       data = {}
       data['clientes'] = []
       data['clientes'].append({
           'informacion': message.text,
           'usuario':mensaje,
           'status':'Pendiente'

           })
       if os.stat("reporte.json").st_size == 0:
          print("Vacío")
          with open('reporte.json', 'w') as file:
               json.dump(data, file, indent=4)
       else:
          with open('reporte.json', 'r+') as file:

               file_content = json.load(file)
               file_content['clientes'].append({'informacion': message.text,'usuario':mensaje,'status':'Pendiente'})
               file.seek(0)
               json.dump(file_content, file, indent=4)
               destino.clear()
               clientes.clear()
               denominacion.clear()
               origen.clear()
               letra.clear()
               tasa.clear()
               envio.clear()
       guarda_datos(mensaje)
    bot.send_message(cid, "Gracias por usar nuestros sistemas, envie el capture del pago al administrador "+admin+",para completar su solicitud y en breve recibira su dinero ", reply_markup=markup)
@bot.message_handler(commands=['info', 'start'])
def thread_main(message):
    a=Thread(target=count, args=(message,))
    threads.append(a)
    a.start()

    #Thread(target=respuesta_botones_inline, args=(message,)).start()
@bot.callback_query_handler(func=lambda x:True)
def thread_maintwo(call):
    b=Thread(target=respuesta_botones_inline, args=(call,))
    b.start()

@bot.message_handler(commands=['ARGENTINA_BRASIL'])
def thread_maintre(message):
    c=Thread(target=cantidadAB, args=(message,))
    threads.append(c)
    c.start()

@bot.message_handler(commands=['ARGENTINA_CHILE'])
def thread_mainfour(message):
    d=Thread(target=cantidadAC, args=(message,))
    threads.append(d)
    d.start()
@bot.message_handler(commands=['ARGENTINA_ESPANA'])
def thread_mainfour(message):
    d=Thread(target=cantidadAES, args=(message,))
    threads.append(d)
    d.start()
@bot.message_handler(func=lambda f: True)
def thread_mainfive(message):
    e=Thread(target=procesar_solicitud, args=(message,))
    threads.append(e)
    e.start()

def thread_mainsix(m):
    f=Thread(target=transaccionAB, args=(m,))
    g=Thread(target=transaccionAC, args=(m,))
    h=Thread(target=transaccionAES, args=(m,))
    g.start()
    f.start()
    h.start()


print("Done!")
bot.polling(non_stop=True,timeout=600)

#asyncio.run(bot.polling(restart_on_change=True))


