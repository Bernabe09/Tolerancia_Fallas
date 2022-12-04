import requests
from WebScraping import  precioaActual 
from WebScraping import  precioDeseado 

def telegram_bot_sendtext(bot_message):

    bot_token  = '5961515340:AAEvHJJXFx4-eB9U-UA9OveacVnEuQ6MoCs'

    bot_chatID = '1561089908'

    enviar_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(enviar_text)

    return response.json()

if precioaActual < precioDeseado:
    texto = f"¡ATENCION! Hay oferta, bajo el precio! Esta en: {str(precioaActual)}"
else:
    texto= f"¡El precio sigue muy alto! Esta en:  {str(precioaActual)}" 
telegram_bot_sendtext(texto)
