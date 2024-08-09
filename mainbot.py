import telebot
from telebot.types import ReplyKeyboardMarkup , KeyboardButton, InlineKeyboardMarkup, Update, InlineKeyboardButton
import requests
from telebot import types
from metodo2 import exportarsheets
from datetime import date
from datetime import datetime
import json,os
bot = telebot.TeleBot("7259921955:AAGZTb-IQAXwMgVjUYzclhZZUmJkmZSCkCY")
hideBoard = types.ReplyKeyboardRemove()
admin=[]
clientes=[]
votaciones=[]
pedidos=[]
text_pedidos={}
clientes_step={}
nombre={}
apodo={}
destino=[]
tasa=[]
denominacion=[]
@bot.message_handler(commands=['info', 'start'])
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
    bot.send_message(message.chat.id,"Bienvenido a nuestra casa de cambio IBG,nuestros bots con inteligencia artificial seran los encargados de atenderlos,PAISES CON LOS QUE TRABAJAMOS, POR FAVOR PULSE EL PAIS DESDE DONDE ENVIA..." ,reply_markup=markup)

@bot.callback_query_handler(func=lambda x:True)
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
@bot.message_handler(commands=['ARGENTINA_BRASIL'])        
def cantidadAB(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/ARGENTINA_BRASIL':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionAB) 
def transaccionAB(m):
    cid = m.chat.id
    entrada=m.text
    tasas=0.0039
    try:
        entrada = int(entrada)
        total=(int(entrada)*0.0039)
        clientes.append(total)
        destino.append('BRASIL')
        tasa.append(tasas)
        bot.send_message(cid,"La tasa de cambio para Brasil es de 0,0039 Reais por peso argentino, usted recibira un total de:"+ str(total) +" reais, pulse el comando /Procesar ,para procesar transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionAB)
@bot.message_handler(commands=['ARGENTINA_CHILE'])        
def cantidadAC(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/ARGENTINA_CHILE':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionAC) 
def transaccionAC(m):
    cid = m.chat.id
    entrada=m.text
    tasas=0.720
    try:
        entrada = int(entrada)
        total=(int(entrada)*0.720)
        print(total)       
        clientes.append(total)
        destino.append('CHILE')
        tasa.append(tasas)
        bot.send_message(cid,"la tasa de cambio para Chile  es de 0,720 Peso chileno por peso argentino, usted recibira un total de:"+ str(total) +" pesos, pulse el comando /Procesar")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionAC)
@bot.message_handler(commands=['ARGENTINA_ESPANA'])        
def cantidadAES(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/ARGENTINA_ESPANA':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionAES) 
def transaccionAES(m):
    cid = m.chat.id
    entrada=m.text
    tasas=0.0007
    try:
         entrada = int(entrada)
         total=(int(entrada)*0.0007)
         print(total)
         clientes.append(total)
         tasa.append(tasas)
         destino.append('ESPAÑA')
         bot.send_message(cid,"la tasa de cambio para España  es de 0,0007 Euro por peso argentino, usted recibira un total de:"+ str(total) +" euros, pulse el comando /Procesar")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionAES)
@bot.message_handler(commands=['ARGENTINA_EEUU'])        
def cantidadAEU(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/ARGENTINA_EEUU':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionAEU) 
def transaccionAEU(m):
    cid = m.chat.id
    entrada=m.text
    tasas=0.0008
    try:
        entrada = int(entrada)
        total=(int(entrada)*0.0008)
        print(total)
        tasa.append(tasas)
        clientes.append(total)
        destino.append('EEUU')
        bot.send_message(cid,"la tasa de cambio para EEUU  es de 0,0008 Dolares por peso argentino, usted recibira un total de:"+ str(total) +" dolares, pulse el comando /Procesar")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionAEU)
@bot.message_handler(commands=['ARGENTINA_USA'])        
def cantidadAUS(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/ARGENTINA_USA':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionAUS) 
def transaccionAUS(m):
    cid = m.chat.id
    entrada=m.text
    tasas=35
    try:
        entrada = int(entrada)
        total=(int(entrada)*35)
        print(total)
        tasa.append(tasas)
        clientes.append(total)
        destino.append('USA')
        bot.send_message(cid,"la tasa de cambio para USA  es de 35 Dolares por peso argentino, usted recibira un total de:"+ str(total) +" dolares, pulse el comando /Procesar")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionAUS)
@bot.message_handler(commands=['ARGENTINA_PANAMA'])        
def cantidadAPAN(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/ARGENTINA_PANAMA':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionAPAN) 
def transaccionAPAN(m):
    cid = m.chat.id
    entrada=m.text
    tasas=0.0008
    try:
        entrada = int(entrada)
        total=(int(entrada)*0.0008)
        print(total)
        tasa.append(tasas)
        clientes.append(total)
        destino.append('PANAMA')
        bot.send_message(cid,"la tasa de cambio para Panama  es de 0,0008 Dolar Panama por peso argentino, usted recibira un total de:"+ str(total) +" dolares, pulse el comando /Procesar")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionAPAN)
@bot.message_handler(commands=['ARGENTINA_PERU'])        
def cantidadAPER(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/ARGENTINA_PERU':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionAPER) 
def transaccionAPER(m):
    cid = m.chat.id
    entrada=m.text
    tasas=0.0029
    try:
        entrada = int(entrada)
        total=(int(entrada)*0.0029)
        print(total)
        tasa.append(tasas)
        clientes.append(total)
        destino.append('PERU')
        bot.send_message(cid,"la tasa de cambio para Peru  es de 0,0029 Soles por peso argentino, usted recibira un total de:"+ str(total) +" soles, pulse el comando /Procesar")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionAPER)    
@bot.message_handler(commands=['ARGENTINA_USDT'])        
def cantidadAUSDT(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/ARGENTINA_USDT':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionAUSDT) 
def transaccionAUSDT(m):
    cid = m.chat.id
    entrada=m.text
    tasas=35
    try:
         entrada = int(entrada)
         total=(int(entrada)*35)
         print(total)
         tasa.append(tasas)
         clientes.append(total)
         destino.append('USDT')
         bot.send_message(cid,"la tasa de cambio para USDT  es de 35 USDT por peso argentino, usted recibira un total de:"+ str(total) +" USDT, pulse el comando Procesar")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionAUSDT) 
@bot.message_handler(commands=['ARGENTINA_VENEZUELA'])        
def cantidadAVES(message):
     nombre=message.text
     cid = message.chat.id
     if cid > 0 and nombre == '/ARGENTINA_VENEZUELA':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionAVES) 
def transaccionAVES(m):
    cid = m.chat.id
    entrada=m.text
    tasas=0.0309
    try:
        entrada = int(entrada)
        total=(int(entrada)*0.0309)
        clientes.append(total)
        tasa.append(tasas)
        destino.append('VENEZUELA')
        msg = bot.send_message(cid, "la tasa de cambio para Venezuela  es de 0,0309 Bolivares por peso argentino, usted recibira un total de: "+ str(total) +" bs pulse el comando /Procesar")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionAVES) 
#region envio desde brasil                                                        

@bot.message_handler(commands=['BRASIL_ARGENTINA'])        
def cantidadBA(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/BRASIL_ARGENTINA':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionBA) 
def transaccionBA(m):
    cid = m.chat.id
    entrada=m.text
    tasas=234.55
    try:
        entrada = int(entrada)
        total=(int(entrada)*234.55)
        clientes.append(total)
        tasa.append(tasas)
        destino.append('ARGENTINA')
        bot.send_message(cid,"la tasa de cambio para Argentina  es de 234,55 Peso argentino reais, usted recibira un total de:"+ str(total) +" , pulse el comando /Procesar ,para procesar transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionBA) 
@bot.message_handler(commands=['BRASIL_CHILE'])        
def cantidadBC(message):
     nombre=message.text
     cid = message.chat.id
     if cid > 0 and nombre == '/BRASIL_CHILE':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionAC) 
def transaccionBC(m):
    cid = m.chat.id
    entrada=m.text
    tasas=166.36
    try:
        entrada = int(entrada)
        total=(int(entrada)*166.36)
        tasa.append(tasas)
        print(total)
        destino.append('CHILE')
        clientes.append(total)
        bot.send_message(cid,"la tasa de cambio para Chile  es de 166,36 Pesos chileno por reais, usted recibira un total de:"+ str(total) +" , pulse el comando /Procesar ,para procesar transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionBC) 
@bot.message_handler(commands=['BRASIL_ESPANA'])        
def cantidadBES(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/BRASIL_ESPANA':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionBES) 
def transaccionBES(m):
    cid = m.chat.id
    entrada=m.text
    tasas=0.168
    try:
        entrada = int(entrada)
        total=(int(entrada)*0.168)
        tasa.append(tasas)
        print(total)
        clientes.append(total)
        destino.append('ESPAÑA')
        bot.send_message(cid,"la tasa de cambio para España  es de 0,168 Euro por Reais, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionBES)
@bot.message_handler(commands=['BRASIL_EEUU'])        
def cantidadBEU(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/BRASIL_EEUU':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionBEU) 
def transaccionBEU(m):
    cid = m.chat.id
    entrada=m.text
    tasas=0.182
    try:
        entrada = int(entrada)
        total=(int(entrada)*0.182)
        tasa.append(tasas)
        print(total)
        clientes.append(total)
        destino.append('EEUU')
        bot.send_message(cid,"la tasa de cambio para EEUU  es de 0,182 Dolares por Reais, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionBEU)
@bot.message_handler(commands=['BRASIL_USA'])        
def cantidadBUS(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/BRASIL_USA':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionBUS) 
def transaccionBUS(m):
    cid = m.chat.id
    entrada=m.text
    tasas=0.35
    try: 
        entrada = int(entrada)
        total=(int(entrada)*35)
        clientes.append(total)
        tasa.append(tasas)
        destino.append('USA')
        print(total)
        bot.send_message(cid,"la tasa de cambio para USA  es de 35 Dolares por Reais, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionBUS)
@bot.message_handler(commands=['BRASIL_PANAMA'])        
def cantidadBPAN(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/BRASIL_PANAMA':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionBPAN) 
def transaccionBPAN(m):
    cid = m.chat.id
    entrada=m.text
    tasas=0.182
    try:
        entrada = int(entrada)
        total=(int(entrada)*0.182)
        clientes.append(total)
        tasa.append(tasas)
        destino.append('PANAMA')
        print(total)
        bot.send_message(cid,"la tasa de cambio para Panama  es de 0,182 Dolar Panama por Reais, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionBPAN)
@bot.message_handler(commands=['BRASIL_PERU'])        
def cantidadBPER(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/BRASIL_PERU':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionBPER) 
def transaccionBPER(m):
    cid = m.chat.id
    entrada=m.text
    tasas=0.665
    try:
        entrada = int(entrada)
        total=(int(entrada)*0.665)
        clientes.append(total)
        tasa.append(tasas)
        destino.append('PERU')
        print(total)
        bot.send_message(cid,"la tasa de cambio para Peru  es de 0,665 Soles por Reais, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionBPER)
@bot.message_handler(commands=['BRASIL_USDT'])        
def cantidadABSDT(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/BRASIL_USDT':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionBUSDT) 
def transaccionBUSDT(m):
    cid = m.chat.id
    entrada=m.text
    tasas=35
    try:
        entrada = int(entrada)
        total=(int(entrada)*35)
        tasa.append(tasas)
        destino.append('USDT')
        print(total)
        clientes.append(total)
        bot.send_message(cid,"la tasa de cambio para USDT  es de 35 USDT por Reais, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionBUSDT)
@bot.message_handler(commands=['BRASIL_VENEZUELA'])        
def cantidadBVES(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/BRASIL_VENEZUELA':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionBVES) 
def transaccionBVES(m):
    cid = m.chat.id
    entrada=m.text
    tasas=7.14
    try:
       entrada = int(entrada)
       total=(int(entrada)*7.14)
       destino.append('VENEZUELA')
       tasa.append(tasas)
       print(total)
       clientes.append(total)
       bot.send_message(cid,"la tasa de cambio para Venezuela  es de 7,14 Bolivares por Reais, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionBVES)
#region envio desde CHILE   
@bot.message_handler(commands=['CHILE_BRASIL'])        
def cantidadCCHI(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/CHILE_BRASIL':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionCCHI) 
def transaccionCCHI(m):
    cid = m.chat.id
    entrada=m.text
    tasas=0.0053
    try:
        entrada = int(entrada)
        total=(int(entrada)*0.0053)
        tasa.append(tasas)
        destino.append('BRASIL')
        print(total)
        clientes.append(total)
        bot.send_message(cid,"la tasa de cambio para Brasil  es de 0,0053 Reais por peso chileno, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionCCHI)
@bot.message_handler(commands=['CHILE_ARGENTINA'])        
def cantidadCARG(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/CHILE_ARGENTINA':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionCARG) 
def transaccionCARG(m):
    cid = m.chat.id
    entrada=m.text
    tasas=1.377
    try:
        entrada = int(entrada)
        total=(int(entrada)*1.377)
        tasa.append(tasas)
        print(total)
        destino.append('ARGENTINA')
        clientes.append(total)
        bot.send_message(cid,"la tasa de cambio para Argentina es de 1,377 Peso argentino por peso chileno, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionCARG)
@bot.message_handler(commands=['CHILE_ESPANA'])        
def cantidadCESP(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/CHILE_ESPANA':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionCESP) 
def transaccionCESP(m):
    cid = m.chat.id
    entrada=m.text
    tasas=0.000987
    try:
        entrada = int(entrada)
        total=(int(entrada)*0.000987)
        print(total)
        tasa.append(tasas)
        destino.append('ESPAÑA')
        clientes.append(total)
        bot.send_message(cid,"la tasa de cambio para España  es de 0,000987 Euros por peso chileno, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionCESP)
@bot.message_handler(commands=['CHILE_EEUU'])        
def cantidadCEEUU(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/CHILE_EEUU':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionCEEUU) 
def transaccionCEEUU(m):
    cid = m.chat.id
    entrada=m.text
    tasas=0.001067
    try:
        entrada = int(entrada)
        total=(int(entrada)*0.001067)
        print(total)
        tasa.append(tasas)
        destino.append('EEUU')
        clientes.append(total)
        bot.send_message(cid,"la tasa de cambio para EEUU es de 0,001067 Dolares por peso Chileno, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionCEEUU)
@bot.message_handler(commands=['CHILE_USA'])        
def cantidadCUSA(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/CHILE_USA':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionCUSA) 
def transaccionCUSA(m):
    cid = m.chat.id
    entrada=m.text
    tasas=35
    try:
        entrada = int(entrada)
        total=(int(entrada)*35)
        print(total)
        tasa.append(tasas)
        destino.append('USA')
        clientes.append(total)
        bot.send_message(cid,"la tasa de cambio para USA  es de 35 Dolares por peso chileno, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionCUSA)
@bot.message_handler(commands=['CHILE_PANAMA'])        
def cantidadCPAN(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/CHILE_PANAMA':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . " ,reply_markup=hideBoard)    
        bot.register_next_step_handler( jid, transaccionCPAN) 
def transaccionCPAN(m):
    cid = m.chat.id
    entrada=m.text
    tasas=0.001067
    try:
        entrada = int(entrada)
        total=(int(entrada)*0.001067)
        print(total)
        destino.append('PANAMA')
        tasa.append(tasas)
        clientes.append(total)
        bot.send_message(cid,"la tasa de cambio para Panama  es de 0,001067 Dolar Panama por peso chileno, usted recibira un total de:"+ str(total) +" , pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionCPAN)
@bot.message_handler(commands=['CHILE_PERU'])        
def cantidadCPER(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/CHILE_PERU':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionCPER) 
def transaccionCPER(m):
    cid = m.chat.id
    entrada=m.text
    tasas=0.00391
    try:
        entrada = int(entrada)
        total=(int(entrada)*0.00391)
        print(total)
        clientes.append(total)
        tasa.append(tasas)
        destino.append('PERU')
        bot.send_message(cid,"la tasa de cambio para Peru es de 0,00391 Soles por peso chileno, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionCPER)
@bot.message_handler(commands=['CHILE_USDT'])        
def cantidadCUSDT(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/CHILE_USDT':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionCUSDT) 
def transaccionCUSDT(m):
    cid = m.chat.id
    entrada=m.text
    tasas=35
    try:
        entrada = int(entrada)
        total=(int(entrada)*35)
        print(total)
        tasa.append(tasas)
        destino.append('USDT')
        clientes.append(total)
        bot.send_message(cid,"la tasa de cambio para USDT  es de 35 Dolares por peso chileno, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionCUSDT)
@bot.message_handler(commands=['CHILE_VENEZUELA'])        
def cantidadCVEN(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/CHILE_VENEZUELA':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionCVEN) 
def transaccionCVEN(m):
    cid = m.chat.id
    entrada=m.text
    tasas=0.0419
    try:
        entrada = int(entrada)
        total=(int(entrada)*0.0419)
        print(total)
        tasa.append(tasas)
        destino.append('VENEZUELA')
        clientes.append(total)
        bot.send_message(cid,"la tasa de cambio para Venezuela  es de 0,0419 Bolivares por peso chileno, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionCVEN)
#REGION ENVIO DESDE ESPAÑA
@bot.message_handler(commands=['ESPAÑA_BRASIL'])        
def cantidadESPB(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/ESPAÑA_BRASIL':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionESPB) 
def transaccionESPB(m):
    cid = m.chat.id
    entrada=m.text
    tasas=5.086
    try:
        entrada = int(entrada)
        total=(int(entrada)*5.086)
        print(total)
        tasa.append(tasas)
        destino.append('BRASIL')
        clientes.append(total)
        bot.send_message(cid,"la tasa de cambio para Brasil  es de 5,086 Reais por euro, usted recibira un total de:"+ str(total) +" , pulse el comando /Procesar ,para procesar transaccion")                            
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionESPB)
@bot.message_handler(commands=['ESPAÑA_ARGENTINA'])        
def cantidadESPA(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/ESPAÑA_ARGENTINA':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionESPA) 
def transaccionESPA(m):
    cid = m.chat.id
    entrada=m.text
    tasas=1312.31
    try:
        entrada = int(entrada)
        total=(int(entrada)*1312.31)
        print(total)
        tasa.append(tasas)
        destino.append('ARGENTINA')
        clientes.append(total)
        bot.send_message(cid,"la tasa de cambio para Argentina  es de 1312,31 Peso argentino por euro, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionESPA)
@bot.message_handler(commands=['ESPAÑA_CHILE'])        
def cantidadESPCHI(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/ESPAÑA_CHILE':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionESPCHI) 
def transaccionESPCHI(m):
    cid = m.chat.id
    entrada=m.text
    tasas=930.82
    try:
        entrada = int(entrada)
        total=(int(entrada)*930.82)
        print(total)
        tasa.append(tasas)
        destino.append('CHILE')
        clientes.append(total)
        bot.send_message(cid,"la tasa de cambio para Chile  es de 930,82 Peso argentino por euro, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionESPCHI)
@bot.message_handler(commands=['ESPAÑA_EEUU'])        
def cantidadESPEEUU(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/ESPAÑA_EEUU':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionESPEEUU) 
def transaccionESPEEUU(m):
    cid = m.chat.id
    entrada=m.text
    tasas=1.017
    try:
        entrada = int(entrada)
        total=(int(entrada)*1.017)
        print(total)
        destino.append('EEUU')
        tasa.append(tasas)
        clientes.append(total)
        bot.send_message(cid,"la tasa de cambio para EEUU  es de 1,017 Dolares por euro, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionESPEEUU)
@bot.message_handler(commands=['ESPAÑA_USA'])        
def cantidadESPUSA(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/ESPAÑA_USA':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionESPUSA) 
def transaccionESPUSA(m):
    cid = m.chat.id
    entrada=m.text
    tasas=35
    try:
        entrada = int(entrada)
        total=(int(entrada)*35)
        print(total)
        destino.append('USA')
        tasa.append(tasas)
        clientes.append(total)
        bot.send_message(cid,"la tasa de cambio para USA  es de 35 Dolares por euro, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionESPUSA)
@bot.message_handler(commands=['ESPANA_PANAMA'])        
def cantidadESPPAN(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/ESPANA_PANAMA':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionESPPAN) 
def transaccionESPPAN(m):
    cid = m.chat.id
    entrada=m.text
    tasas=1.017
    try:
        entrada = int(entrada)
        total=(int(entrada)*1.017)
        print(total)
        tasa.append(tasas)
        destino.append('PANAMA')
        clientes.append(total)
        bot.send_message(cid,"la tasa de cambio para Panama  es de 1,017 Dolar Panama por euro, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionESPPAN)
#REGION ENVIO DESDE EEUU
@bot.message_handler(commands=['EEUU_BRASIL'])        
def cantidadEEUUBR(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/EEUU_BRASIL':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionEEUUBR) 
def transaccionEEUUBR(m):
    cid = m.chat.id
    entrada=m.text
    tasas=5.000
    try:
        entrada = int(entrada)
        total=(int(entrada)*5.000)
        print(total)
        tasa.append(tasas)
        destino.append('BRASIL')
        clientes.append(total)
        bot.send_message(cid,"la tasa de cambio para Brasil  es de 5,000 Reais por dolar, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionEEUUBR)
@bot.message_handler(commands=['EEUU_ARGENTINA'])        
def cantidadEEUUAR(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/EEUU_ARGENTINA':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionEEUUAR) 
def transaccionEEUUAR(m):
    cid = m.chat.id
    entrada=m.text
    tasas=1290.000
    try:
        entrada = int(entrada)
        total=(int(entrada)*1290.000)
        print(total)
        clientes.append(total)
        destino.append('ARGENTINA')
        tasa.append(tasas)
        bot.send_message(cid,"la tasa de cambio para Argentina  es de 1290,000 Peso argentino por dolar, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionEEUUAR)
@bot.message_handler(commands=['EEUU_CHILE'])        
def cantidadEEUUCH(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/EEUU_CHILE':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionEEUUCH) 
def transaccionEEUUCH(m):
    cid = m.chat.id
    entrada=m.text
    tasas=915.00
    try:
        entrada = int(entrada)
        total=(int(entrada)*915.00)
        print(total)
        destino.append('CHILE')
        tasa.append(tasas)
        clientes.append(total)
        bot.send_message(cid,"la tasa de cambio para Chile  es de 915,00 Peso chileno por dolar, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionEEUUCH)
@bot.message_handler(commands=['EEUU_ESPAÑA'])        
def cantidadEEUUESP(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/EEUU_ESPAÑA':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionEEUUESP) 
def transaccionEEUUESP(m):
    cid = m.chat.id
    entrada=m.text
    tasas=0.93
    try:
        entrada = int(entrada)
        total=(int(entrada)*0.93)
        print(total)
        destino.append('ESPAÑA')
        tasa.append(tasas)
        clientes.append(total)
        bot.send_message(cid,"la tasa de cambio para España  es de 0,93 Euro por dolar, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionEEUUESP)
@bot.message_handler(commands=['EEUU_USA'])        
def cantidadEEUUBR(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/EEUU_USA':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionEEUUUSA) 
def transaccionEEUUUSA(m):
    cid = m.chat.id
    entrada=m.text
    tasas=35
    try:
       entrada = int(entrada)
       total=(int(entrada)*35)
       print(total)
       tasa.append(tasas)
       destino.append('USA')
       clientes.append(total)
       bot.send_message(cid,"la tasa de cambio para USA  es de 35 dolares por dolar, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionEEUUUSA) 
@bot.message_handler(commands=['EEUU_PANAMA'])        
def cantidadEEUUPAN(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/EEUU_PANAMA':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionEEUUPAN) 
def transaccionEEUUPAN(m):
    cid = m.chat.id
    entrada=m.text
    tasas=1.00
    try:
         entrada = int(entrada)
         total=(int(entrada)*1.00)
         print(total)
         destino.append('PANAMA')
         tasa.append(tasas)
         clientes.append(total)
         bot.send_message(cid,"la tasa de cambio para Panama  es de 1,00 Dolar Panama por dolar, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionEEUUUSA) 
@bot.message_handler(commands=['EEUU_PERU'])        
def cantidadEEUUPER(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/EEUU_PERU':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionEEUUBR) 
def transaccionEEUUPER(m):
    cid = m.chat.id
    entrada=m.text
    tasas=3.660
    try:
        entrada = int(entrada)
        total=(int(entrada)*3.660)
        print(total)
        tasa.append(tasas)
        destino.append('PERU')
        clientes.append(total)
        bot.send_message(cid,"la tasa de cambio para Peru  es de 3,660 Soles por dolar, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionEEUUPER)
@bot.message_handler(commands=['EEUU_USDT'])        
def cantidadEEUUUSDT(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/EEUU_USDT':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionEEUUUSDT) 
def transaccionEEUUUSDT(m):
    cid = m.chat.id
    entrada=m.text
    tasas=35
    try:
        entrada = int(entrada)
        total=(int(entrada)*35)
        print(total)
        tasa.append(tasas)
        destino.append('USDT')
        clientes.append(total)
        bot.send_message(cid,"la tasa de cambio para USDT  es de 35 dolares por dolar, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionEEUUUSDT)
@bot.message_handler(commands=['EEUU_VENEZUELA'])        
def cantidadEEUUVEN(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/EEUU_VENEZUELA':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionEEUUVEN) 
def transaccionEEUUVEN(m):
    cid = m.chat.id
    entrada=m.text
    tasas=39.25
    try:
         entrada = int(entrada)
         total=(int(entrada)*39.25)
         print(total)
         clientes.append(total)
         destino.append('VENEZUELA')
         bot.send_message(cid,"la tasa de cambio para Venezuela  es de 39,25 Bolivares por dolar, usted recibira un total de:"+ str(total) +" , pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionEEUUVEN)
#REGION ENVIO DESDE USA
@bot.message_handler(commands=['USA_BRASIL'])        
def cantidadUSABR(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/USA_BRASIL':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionUSABR) 
def transaccionUSABR(m):
    cid = m.chat.id
    entrada=m.text
    tasas=35
    try:
        entrada = int(entrada)
        total=(int(entrada)*35)
        print(total)
        tasa.append(tasas)
        destino.append('BRASIL')
        clientes.append(total)
        bot.send_message(cid,"la tasa de cambio para Brasil  es de 35 Reais por dolar, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionUSABR)
@bot.message_handler(commands=['USA_ARGENTINA'])        
def cantidadUSAAR(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/USA_ARGENTINA':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionUSAAR) 
def transaccionUSAAR(m):
    cid = m.chat.id
    entrada=m.text
    tasas=35
    try:
        entrada = int(entrada)
        total=(int(entrada)*35)
        print(total)
        destino.append('ARGENTINA')
        tasa.append(tasas)
        clientes.append(total)
        bot.send_message(cid,"la tasa de cambio para Argentina  es de 35 Pesos argentinos por dolar, usted recibira un total de:"+ str(total) +" , pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionUSAAR)
@bot.message_handler(commands=['USA_CHILE'])        
def cantidadUSACHI(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/USA_CHILE':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionUSACHI) 
def transaccionUSACHI(m):
    cid = m.chat.id
    entrada=m.text
    tasas=35
    try:
        entrada = int(entrada)
        total=(int(entrada)*35)
        print(total)
        destino.append('CHILE')
        tasa.append(tasas)
        clientes.append(total)
        bot.send_message(cid,"la tasa de cambio para Chile  es de 35 Pesos chilenos por dolar, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionUSACHI)
@bot.message_handler(commands=['USA_ESPAÑA'])        
def cantidadUSAESP(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/USA_ESPAÑA':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionUSAESP) 
def transaccionUSAESP(m):
    cid = m.chat.id
    entrada=m.text
    tasas=35
    try:
         entrada = int(entrada)
         total=(int(entrada)*35)
         print(total)
         tasa.append(tasas)
         destino.append('ESPAÑA')
         clientes.append(total)
         bot.send_message(cid,"la tasa de cambio para España  es de 35 Euros por peso dolar, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionUSAESP)
@bot.message_handler(commands=['USA_EEUU'])        
def cantidadUSAEEUU(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/USA_EEUU':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionUSAEEUU) 
def transaccionUSAEEUU(m):
    cid = m.chat.id
    entrada=m.text
    tasas=35
    try:
        entrada = int(entrada)
        total=(int(entrada)*35)
        print(total)
        tasa.append(tasas)
        destino.append('EEUU')
        clientes.append(total)
        bot.send_message(cid,"la tasa de cambio para EEUU  es de 35 dolares por peso dolar, usted recibira un total de:"+ str(total) +" , pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionUSAEEUU)
@bot.message_handler(commands=['USA_PANAMA'])        
def cantidadUSAPAN(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/USA_PANAMA':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionUSAPAN) 
def transaccionUSAPAN(m):
    cid = m.chat.id
    entrada=m.text
    tasas=35
    try:
         entrada = int(entrada)
         total=(int(entrada)*35)
         print(total)
         clientes.append(total)
         tasa.append(tasas)
         destino.append('PANAMA')
         bot.send_message(cid,"la tasa de cambio para Panama  es de 35 Dolar Panama por peso dolar, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionUSAPAN)
@bot.message_handler(commands=['USA_PERU'])        
def cantidadUSAPERU(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/USA_PERU':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionUSAPERU) 
def transaccionUSAPERU(m):
    cid = m.chat.id
    entrada=m.text
    tasas=35
    try:
        entrada = int(entrada)
        total=(int(entrada)*35)
        print(total)
        destino.append('PERU')
        clientes.append(total)
        tasa.append(tasas)
        bot.send_message(cid,"la tasa de cambio para Peru  es de 35 Soles por dolar, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionUSAPERU)
@bot.message_handler(commands=['USA_USDT'])        
def cantidadUSAUSDT(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/USA_USDT':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionUSAUSDT) 
def transaccionUSAUSDT(m):
    cid = m.chat.id
    entrada=m.text
    tasas=35
    try:
        entrada = int(entrada)
        total=(int(entrada)*35)
        print(total)
        destino.append('USDT')
        clientes.append(total)
        tasa.append(tasas)
        bot.send_message(cid,"la tasa de cambio para USDT  es de 35 dolares por peso dolar, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionUSAUSDT)
@bot.message_handler(commands=['USA_VENEZUELA'])        
def cantidadUSAVENEZUELA(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/USA_VENEZUELA':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionUSAVENEZUELA) 
def transaccionUSAVENEZUELA(m):
    cid = m.chat.id
    entrada=m.text
    tasas=35
    try:
        entrada = int(entrada)
        total=(int(entrada)*35)
        print(total)
        destino.append('VENEZUELA')
        clientes.append(total)
        tasa.append(tasas)
        bot.send_message(cid,"la tasa de cambio para Venezuela  es de 35 Bolivares por dolar, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionUSAVENEZUELA)
#REGION ENVIO DESDE PANAMA
@bot.message_handler(commands=['PANAMA_BRASIL'])        
def cantidadPANBR(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/PANAMA_BRASIL':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionPANBR) 
def transaccionPANBR(m):
    cid = m.chat.id
    entrada=m.text
    tasas=5.000
    try:
        entrada = int(entrada)
        total=(int(entrada)*5.000)
        print(total)
        destino.append('BRASIL')
        clientes.append(total)
        tasa.append(tasas)
        bot.send_message(cid,"la tasa de cambio para Brasil  es de 5,000 Reais por Dolar Panama, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionPANBR)
@bot.message_handler(commands=['PANAMA_ARGENTINA'])        
def cantidadPANARG(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/PANAMA_ARGENTINA':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionPANARG) 
def transaccionPANARG(m):
    cid = m.chat.id
    entrada=m.text
    tasas=1290.00
    try:
        entrada = int(entrada)
        total=(int(entrada)*1290.00)
        print(total)
        destino.append('ARGENTINA')
        clientes.append(total)
        tasa.append(tasas)
        bot.send_message(cid,"la tasa de cambio para Argentina  es de 1290,00 Peso argentino por Dolar Panama, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionPANARG)
@bot.message_handler(commands=['PANAMA_CHILE'])        
def cantidadPANCHI(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/PANAMA_CHILE':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionPANCHI) 
def transaccionPANCHI(m):
    cid = m.chat.id
    entrada=m.text
    tasas=915.00
    try:
        entrada = int(entrada)
        total=(int(entrada)*915.00)
        print(total)
        destino.append('CHILE')
        clientes.append(total)
        bot.send_message(cid,"la tasa de cambio para Chile  es de 915,00 Peso chileno por Dolar Panama, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionPANCHI)
@bot.message_handler(commands=['PANAMA_ESPAÑA'])        
def cantidadPANESP(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/PANAMA_ESPAÑA':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionPANESP) 
def transaccionPANESP(m):
    cid = m.chat.id
    entrada=m.text
    tasas=0.925
    try:
        entrada = int(entrada)
        total=(int(entrada)*0.925)
        print(total)
        clientes.append(total)
        tasa.append(tasas)
        destino.append('ESPAÑA')
        bot.send_message(cid,"la tasa de cambio para España  es de 0,925 Euro por Dolar Panama, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionPANESP)
@bot.message_handler(commands=['PANAMA_EEUU'])        
def cantidadPANEEUU(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/PANAMA_EEUU':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionPANEEUU) 
def transaccionPANEEUU(m):
    cid = m.chat.id
    entrada=m.text
    tasas=1.000
    try:
        entrada = int(entrada)
        total=(int(entrada)*1.000)
        print(total)
        clientes.append(total)
        tasa.append(tasas)
        destino.append('EEUU')
        bot.send_message(cid,"la tasa de cambio para EEUU  es de 1,000 Dolar por Dolar Panama, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionPANEEUU)
@bot.message_handler(commands=['PANAMA_USA'])        
def cantidadPANUSA(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/PANAMA_USA':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionPANUSA) 
def transaccionPANUSA(m):
    cid = m.chat.id
    entrada=m.text
    tasas=35
    try:
        entrada = int(entrada)
        total=(int(entrada)*35)
        print(total)
        destino.append('USA')
        tasa.append(tasas)
        clientes.append(total)
        bot.send_message(cid,"la tasa de cambio para USA  es de 35 Dolares por Dolar Panama, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionPANUSA)
@bot.message_handler(commands=['PANAMA_PERU'])        
def cantidadPANPER(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/PANAMA_PERU':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionPANPER) 
def transaccionPANPER(m):
    cid = m.chat.id
    entrada=m.text
    tasas=3.66
    try:
        entrada = int(entrada)
        total=(int(entrada)*3.66)
        print(total)
        destino.append('PERU')
        tasa.append(tasas)
        clientes.append(total)
        bot.send_message(cid,"la tasa de cambio para Peru  es de 3,66 Soles por Dolar Panama, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionPANPER)
@bot.message_handler(commands=['PANAMA_USDT'])        
def cantidadPANUSDT(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/PANAMA_USDT':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionPANUSDT) 
def transaccionPANUSDT(m):
    cid = m.chat.id
    entrada=m.text
    tasas=35
    try:
        entrada = int(entrada)
        total=(int(entrada)*35)
        print(total)
        destino.append('USDT')
        tasa.append(tasas)
        clientes.append(total)
        bot.send_message(cid,"la tasa de cambio para USDT  es de 35 Dolares por Dolar Panama, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionPANUSDT)
@bot.message_handler(commands=['PANAMA_VENEZUELA'])        
def cantidadPANVEN(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/PANAMA_VENEZUELA':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionPANVEN) 
def transaccionPANVEN(m):
    cid = m.chat.id
    entrada=m.text
    tasas=39.25
    try:
        entrada = int(entrada)
        total=(int(entrada)*39.25)
        print(total)
        destino.append('VENEZUELA')
        tasa.append(tasas)
        clientes.append(total)
        bot.send_message(cid,"la tasa de cambio para Venezuela  es de 39,25 Bolivares por Dolar Panama, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionPANVEN)
#REGION ENVIO PERU
@bot.message_handler(commands=['PERU_ARGENTINA'])        
def cantidadPERUARG(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/PERU_ARGENTINA':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionPERUARG) 
def transaccionPERUARG(m):
    cid = m.chat.id
    entrada=m.text
    tasas=343.630
    try:
        entrada = int(entrada)
        total=(int(entrada)*343.630)
        print(total)
        tasa.append(tasas)
        destino.append('ARGENTINA')
        clientes.append(total)
        bot.send_message(cid,"la tasa de cambio para Argentina  es de 343,630 Peso argentino por sol, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionPERUARG)
@bot.message_handler(commands=['PERU_BRASIL'])        
def cantidadPERUBR(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/PERU_BRASIL':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionPERUBR) 
def transaccionPERUBR(m):
    cid = m.chat.id
    entrada=m.text
    tasas=1.33
    try:
        entrada = int(entrada)
        total=(int(entrada)*1.33)
        print(total)
        destino.append('BRASIL')
        tasa.append(tasas)
        clientes.append(total)
        bot.send_message(cid,"la tasa de cambio para Brasil  es de 1,33 Reais por sol, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionPERUBR)
@bot.message_handler(commands=['PERU_CHILE'])        
def cantidadPERUCHI(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/PERU_CHILE':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionPERUCHI) 
def transaccionPERUCHI(m):
    cid = m.chat.id
    entrada=m.text
    tasas=243.74
    try:
        entrada = int(entrada)
        total=(int(entrada)*243.74)
        print(total)
        destino.append('CHILE')
        clientes.append(total)
        tasa.append(tasas)
        bot.send_message(cid,"la tasa de cambio para Chile  es de 243,74 Peso chileno por sol, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionPERUCHI)
@bot.message_handler(commands=['PERU_ESPAÑA'])        
def cantidadPERUESP(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/PERU_ESPAÑA':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionPERUESP) 
def transaccionPERUESP(m):
    cid = m.chat.id
    entrada=m.text
    tasas=0.246
    try:
        entrada = int(entrada)
        total=(int(entrada)*0.246)
        print(total)
        destino.append('ESPAÑA')
        tasa.append(tasas)
        clientes.append(total)
        bot.send_message(cid,"la tasa de cambio para Espana  es de 0,246 Euro por sol, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionPERUESP)
@bot.message_handler(commands=['PERU_EEUU'])        
def cantidadPERUEEUU(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/PERU_EEUU':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionPERUEEUU) 
def transaccionPERUEEUU(m):
    cid = m.chat.id
    entrada=m.text
    tasas=0.266
    try:
        entrada = int(entrada)
        total=(int(entrada)*0.266)
        print(total)
        destino.append('EEUU')
        tasa.append(tasas)
        clientes.append(total)
        bot.send_message(cid,"la tasa de cambio para EEUU  es de 0,266 Dolares por sol, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionPERUEEUU)
@bot.message_handler(commands=['PERU_USA'])        
def cantidadPERUSA(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/PERU_USA':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionPERUSA) 
def transaccionPERUSA(m):
    cid = m.chat.id
    entrada=m.text
    tasas=35
    try:
        entrada = int(entrada)
        total=(int(entrada)*35)
        print(total)
        destino.append('USA')
        tasa.append(tasas)
        clientes.append(total)
        bot.send_message(cid,"la tasa de cambio para USA  es de 35 Dolares por sol, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionPERUSA)
@bot.message_handler(commands=['PERU_PANAMA'])        
def cantidadPERUPANAMA(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/PERU_PANAMA':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionPERUPANAMA) 
def transaccionPERUPANAMA(m):
    cid = m.chat.id
    entrada=m.text
    tasas=0.266
    try:
        entrada = int(entrada)
        total=(int(entrada)*0.266)
        print(total)
        destino.append('PANAMA')
        clientes.append(total)
        tasa.append(tasas)
        bot.send_message(cid,"la tasa de cambio para Panama  es de 0,266 Dolar Panama por sol, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionPERUPANAMA)
@bot.message_handler(commands=['PERU_USDT'])        
def cantidadPERUUSDT(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/PERU_USDT':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionPERUBR) 
def transaccionPERUUSDT(m):
    cid = m.chat.id
    entrada=m.text
    tasas=35
    try:
        entrada = int(entrada)
        total=(int(entrada)*35)
        print(total)
        destino.append('USDT')
        tasa.append(tasas)
        clientes.append(total)
        bot.send_message(cid,"la tasa de cambio para USDT  es de 35 Dolares por sol, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionPERUUSDT)
@bot.message_handler(commands=['PERU_VENEZUELA'])        
def cantidadPERUVEN(message):
     print('entro')
     nombre=message.text
     cid = message.chat.id

     if cid > 0 and nombre == '/PERU_VENEZUELA':
        jid=bot.send_message(cid,"Hola, es un placer verte, Introduzca la cantidad a enviar . ",reply_markup=hideBoard )    
        bot.register_next_step_handler( jid, transaccionPERUVEN) 
def transaccionPERUVEN(m):
    cid = m.chat.id
    entrada=m.text
    tasas=10.46
    try:
        entrada = int(entrada)
        total=(int(entrada)*10.46)
        print(total)
        destino.append('VENEZUELA')
        tasa.append(tasas)
        clientes.append(total)
        bot.send_message(cid,"la tasa de cambio para Venezuela  es de 10,46 Bolivares por sol, usted recibira un total de:"+ str(total) +", pulse el comando /Procesar ,para procesar transaccion")                        
    except ValueError:
        jid=bot.send_message(cid,"Por favor introduzca una cantidad valida") 
        bot.register_next_step_handler( jid, transaccionPERUVEN)
@bot.message_handler(commands=['admin'])
def admin_reporte(message):
    cid=message.chat.id 
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
                 cantidad=client['cantidad_a_enviar']
                 denmina=client['denominacion']
                 bot.send_message(cid,"Reportes:"+retorna+" Usuario:"+usuario+" Cantidad:"+str(cantidad)+" Denominacion:"+denmina+" Status:"+status+"")

@bot.message_handler(func=lambda f: True)
def procesar_solicitud(message):
    texto=message.text
    cid = message.chat.id
    if cid > 0  and texto == '/Procesar':
       if destino[0] == 'Argentina':
          valor=clientes[0]
          desti=destino[0]
          denominacion.append('Ars')
          exportarsheets(valor,'I',desti,tasa[0])
          msg=bot.send_message(cid,"Solicitud Procesada, favor enviar los siguientes datos MercadoPago:  CVU: , Nombre del Titular:")                       
          bot.register_next_step_handler(msg,capturar_datos)
       elif destino[0] == 'BRASIL':
          valor=clientes[0]
          desti=destino[0]
          print(tasa[0])
          denominacion.append('Brl')
          exportarsheets(valor,'H',desti,tasa[0])
          msg=bot.send_message(cid,"Solicitud Procesada, favor enviar los siguientes datos Brasil Pix:  Chave Pix: ,  Nombre del Titular:")                       
          bot.register_next_step_handler(msg,capturar_datos)
       elif destino[0] == 'CHILE':
          valor=clientes[0]
          desti=destino[0]
          denominacion.append('Clp')
          exportarsheets(valor,'G',desti,tasa[0])
          msg=bot.send_message(cid,"Solicitud Procesada, favor enviar los siguientes datos Transferencia Bancaria:  Nombre del banco: , Nro de cuenta:, cedula:, Correo:, Nombre del Titular:")                       
          bot.register_next_step_handler(msg,capturar_datos)
       elif destino[0] == 'ESPAÑA':
          valor=clientes[0]
          desti=destino[0]
          denominacion.append('Eur')
          exportarsheets(valor,'K',desti,tasa[0])
          msg=bot.send_message(cid,"Solicitud Procesada, favor enviar los siguientes datos Transferencia Bancaria y Bizum:  Nombre del banco: , Nro de cuenta:, telefono:, Correo:, Nombre del Titular:")                       
          bot.register_next_step_handler(msg,capturar_datos)
       elif destino[0] == 'EEUU':
          valor=clientes[0]
          desti=destino[0]
          denominacion.append('Usd')
          exportarsheets(valor,'L',desti,tasa[0])
          msg=bot.send_message(cid,"Solicitud Procesada, favor enviar los siguientes datos ZELLE: Correo electronico:, Nombre del Titular:")                       
          bot.register_next_step_handler(msg,capturar_datos)
       elif destino[0] == 'USA':
          valor=clientes[0]
          desti=destino[0]
          denominacion.append('Usd')
          exportarsheets(valor,'M',desti,tasa[0])
          msg=bot.send_message(cid,"Solicitud Procesada, favor enviar los siguientes datos Transferencia Bancaria:  Nombre del banco: , Nro de cuenta:, cedula:, Correo:, Nombre del Titular:")                       
          bot.register_next_step_handler(msg,capturar_datos)
       elif destino[0] == 'PANAMA':
          valor=clientes[0]
          desti=destino[0]
          denominacion.append('Usd')
          exportarsheets(valor,'L',desti,tasa[0])
          msg=bot.send_message(cid,"Solicitud Procesada, favor enviar los siguientes datos Transferencia Banco general de panama Yappy: Nro de cuenta: Telefono:, Nombre del Titular:")                       
          bot.register_next_step_handler(msg,capturar_datos)
       elif destino[0] == 'PERU':
          valor=clientes[0]
          desti=destino[0]
          denominacion.append('Pen')
          exportarsheets(valor,'F',desti,tasa[0])
          msg=bot.send_message(cid,"Solicitud Procesada, favor enviar los siguientes datos Transferencia Bancaria Yape, Plin: Nombre del Banco:, Nro de cuenta:, telefono:, Correo:, Nombre del Titular:")                       
          bot.register_next_step_handler(msg,capturar_datos)
       elif destino[0] == 'USDT':
          valor=clientes[0]
          desti=destino[0]
          denominacion.append('Usdt')
          exportarsheets(valor,'N',desti,tasa[0])
          msg=bot.send_message(cid,"Solicitud Procesada, favor enviar los siguientes datos Transferencia Bancaria:  Nombre del banco: , Nro de cuenta:, cedula:, Correo:, Nombre del Titular:")                       
          bot.register_next_step_handler(msg,capturar_datos)
       elif destino[0] == 'VENEZUELA':
          valor=clientes[0]
          desti=destino[0]
          denominacion.append('Bs')
          exportarsheets(valor,'E',desti,tasa[0])
          msg=bot.send_message(cid,"Solicitud Procesada, favor enviar los siguientes datos Transferencia Bancaria:  Nombre del banco: , Nro de cuenta:, cedula:, Correo:, Nombre del Titular:")                       
          bot.register_next_step_handler(msg,capturar_datos)
def capturar_datos(message):
    cid = message.chat.id
    print(message.text)
    markup = types.ReplyKeyboardMarkup()
    mensaje =  " (@" + str(message.from_user.username) + ")"
    admin="(@IberoGestion)"
    data = {}
    data['clientes'] = []
    data['clientes'].append({
         'informacion': message.text,
         'usuario':mensaje,
         'status':'Pendiente',
         'cantidad_a_enviar':clientes[0],
         'denominacion':denominacion[0]
         })
    if os.stat("reporte.json").st_size == 0:
       print("Vacío")
       with open('reporte.json', 'w') as file:
            json.dump(data, file, indent=4)
    else:        
       with open('reporte.json', 'r+') as file:
        
            file_content = json.load(file)
            file_content['clientes'].append({'informacion': message.text,'usuario':mensaje,'cantidad_a_enviar':clientes[0],'denominacion':denominacion[0],'status':'Pendiente'})
            file.seek(0)
            json.dump(file_content, file, indent=4)
    bot.send_message(cid, "gracias "+ mensaje +", su Solicitud esta en proceso pronto recibira su dinero, envie el capture del pago al administrador "+admin+"", reply_markup=markup)                   
bot.polling(none_stop=True)
