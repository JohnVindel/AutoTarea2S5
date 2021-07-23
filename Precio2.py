#Tarea 2 - Precios
import telebot 

bot = telebot.TeleBot('1883937208:AAEcgBcQnAmqmw0Pd8Ezfex0NXO8RuaoJIs')
updates = bot.get_updates()
message = updates[0].message
from_user = message.from_user
id = from_user.id
get_me = bot.get_me()

@bot.message_handler(commands=['dolar'])
def info(mensaje):
    bot.reply_to(mensaje, "El precio del dolar es: Compra L.23.7554, Venta L.23.8814")
    print("PrecioDolar")

@bot.message_handler(commands=['euro'])
def info(mensaje):
    bot.reply_to(mensaje, "El precio del dolar es: Compra L.27.6284, Venta L.30.3294")
    print("PrecioEuro")

@bot.message_handler(commands=['cafe'])
def info(mensaje):
    bot.reply_to(mensaje, "El precio del Cafe por quintal es: Lempiras L.3,597.88, Dolar $149.29")
    print("PrecioCafe")

@bot.message_handler(commands=['oro'])
def info(mensaje):
    bot.reply_to(mensaje, "El precio del Oro por onza es: Lempiras L.43,344.67, Dolar $1,808.32")
    print("PrecioOro")

bot.polling()
