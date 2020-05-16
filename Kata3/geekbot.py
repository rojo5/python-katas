from telegram.ext import Updater, CommandHandler

def main():
    updater = Updater(token="768754209:AAHu05Fr-B0OW2LdAsCodZw__fAlsebktH8", use_context=True)
    print("Se ha instanciado")

    #Añadiendo manejador al comando /start
    updater.dispatcher.add_handler(CommandHandler("start", start))

    #Añadir manejador al comadno /repite
    updater.dispatcher.add_handler(CommandHandler("repite", repite))

    #Añador manejador comando /suma
    updater.dispatcher.add_handler(CommandHandler("suma", suma))

    #Pedir notificaciones a Telegram
    updater.start_polling()

    #Notifica al bot que se va acabar
    updater.idle() 


def start(update, context):
    update.message.reply_text("Hello there!")
    
def suma(update, context):
   resultado = int(context.args[0]) + int(context.args[1])
   update.message.reply_text("El resultado es: "+ str(resultado))

def repite(update,context):
    if context.args[0].lower() == "babu":
        update.message.reply_text("Babu Frik? Es uno de mis más viejos amigos")
    else:
        update.message.reply_text(update.message.text)
        


main()