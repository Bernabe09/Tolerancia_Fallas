from bs4 import BeautifulSoup
import requests
import time
import webbrowser

#precioDeseado = int(input("¿Cual es su precio deseado?: "))
#print("Accediendo a la web..")
#time.sleep(2)
#print("Verificando el precio..")
#time.sleep(2)
#print("Aguarde por favor...")
#time.sleep(1)

precioDeseado = 17000

url = requests.get("https://www.mercadolibre.com.mx/laptop-lenovo-ideapad-15alc6-abyss-blue-156-amd-ryzen-5-5500u-8gb-de-ram-256gb-ssd-amd-radeon-rx-vega-7-1920x1080px-windows-10-home/p/MLM18518416?pdp_filters=category:MLM1652#searchVariation=MLM18518416&position=5&search_layout=stack&type=product&tracking_id=ac34ddce-e747-4440-8d6f-099dbdeef01f")
soup = BeautifulSoup(url.content, "html.parser")
resultado = soup.find('span', {'class':'andes-money-amount__fraction'})
precioaActual_text = resultado.text.replace(",","")
precioaActual = float (precioaActual_text)


#precioDeseado = precioDeseado

if precioaActual < precioDeseado:
    print(f" ¡ATENCION! Hay oferta, bajo el precio! Esta en:  {'$'+str(precioaActual)} ")
    #print(" ")
    #i = input('¿Quieres accerder a la web?: ')
    #if i == 'y':

        #webbrowser.open_new_tab(pag)
else:
    print("El precio sigue demasiado alto")