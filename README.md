# Tolerancia Fallas
Este proyecto trata de un BOT que se gestiona por medio de una API de Telegram, todo por medio de de un mismo CHAT de telegram y tener una escalabilidad para al mmismo
y tolerancia a fallas, algunas de las herramientas que se utilizamos fueron Docker, Kubernetes, Istio y por supuesto GitHub.

<div align="center"><img align="center" height="100" alt="image" src="./imagenes/GitHub.jpg"><img align="center" height="100" alt="image" src="./imagenes/docker.png"><img align="center" height="100" alt="image" src="./imagenes/kubernetes.png"><img align="center" height="100" alt="image" src="./imagenes/istio.png"></div>


# Introducción
 Para este proyecto usamos algunas herramientas que aprendimos en nuestro curso de tolerancia a fallas, e implementamos una herrmientas que que descubrimos durante el curso la cual es el <strong>WebScraping</strong> esta es una librería que podemos encontrar en el lenguaje de programación de <i><strong>Python</strong></i>, es una técnica que sirve para extraer información de uno o varios sitios webs de terceros.
 Tambien hacemos uso de una API de telegram que nos permite enlazar enviar notifacaciones al usuario en cuestión. Todo esto por supuesto escalandolo a contenedores,  llevandolo a otros servidores y a monitoriar el trafico entre ellos.
# Requerimientos
 ### Principales herramientas utilizadas para este proyecto

#### Linea de codigo

* $ pip install BeautifulSoup
* $ pip install webbrowser
* $ pip install requests

### ¿Como funcionan estas herramientas?

*1.- BeautifulSoup*

Beautiful Soup es una librería Python que permite extraer información de contenido en formato HTML o XML. Para usarla, es necesario especificar un parser, que es responsable de transformar un documento HTML o XML en un árbol complejo de objetos Python.

*2.- Webbrowser*

Proporciona una interfaz de alto nivel que permite mostrar documentos basados en web a los usuarios. En la mayoría de circunstancias, simplemente llamar a la función open() desde este módulo hará lo correcto.

*3.- request*

Es una biblioteca HTTP para el lenguaje de programación Python. El
objetivo del proyecto es hacer que las solicitudes HTTP sean más simples y
amigables para los humanos.

### ¿Como se espera escalar?

Se planea crear un bot en telegram en el cual mediante un botón de “start” nos permitirá realizar la consulta sin tener que compilarlo desde el editor, el cual nos brinda un token en la consulta para validar la identificación del usuario.

*Telegram*: Utilizamos telegram por la gran cantidad de herramientas que nos proporciona de manera fácil, de igual manera se planea poder escalar a Whatsapp en un futuro ya que como sabemos es la app más frecuentemente utilizada.

<p align="center"><img height="200" alt="image" src="./imagenes/telegram.png"></p>

*BothFather*: Interactuar con BotFather consiste en intercambiar mensajes. Dale a“Start” y te aparecerán una serie de comandos. Cada uno te servirá para personalizar tu bot al máximo. Vamos a crear el bot ejecutando el comando /newbot o dando clic a dicho comando.

<p align="center"><img height="200" alt="image" src="./imagenes/botf.jpg"></p>

# Pasos principales para la realizacion del proyecto
 ## Web Scraping
 En primera instancia lo que hacemos es conseguir los datos de la página web para poder trabajas con ellos, en este caso solo con el dato que requierimos el cual es el precio del producto, es muy sencillo el generar la lectura en este caso para el programa solo es necesario identificar un objeto, para este caso es necesario indicar al programa cual objeto de <i>HTML</i> es el que nos interesa. 

 <p align="center"><img align="center" height="350" alt="image" src="./imagenes/mercadoLibreModoProgramador.png"></p>

De este aparta obtendremos mas que nada el bloque donde se almacena el precio del producto, ya que es la unica instacia que ocupamos para saber si el precio bajo de valor o no.


 ## Configuracion del bot-telegram

En este aparatado configuramos nuestro bot con los datos y valores unicos que nos brinda esta herramienta una ves creada.

 Lo principal que obtendremos de este aparatado es:

 - Token
 - Id  (identificador)

<p align="center"><img align="center" height="250" alt="image" src="./imagenes/conf1.png"></p>

Una ves obtenido este apartado lo agregaremos en la parte del codigo correspondiente, esto mas que nada para enlazar tanto el codigo ejecutable del VSCode y el bot de telegram.

 <p align="center"><img align="center" height="200" alt="image" src="./imagenes/conbot.png"></p>
 
 # Implementacion Docker
 
 Docker es un sistema operativo (o runtime) para contenedores. El motor de Docker se instala en cada servidor en el que desee ejecutar contenedores y proporciona un conjunto sencillo de comandos que puede utilizar para crear, iniciar o detener contenedores.
 
<p align="center"><img align="center" height="250" alt="image" src="./imagenes/CreacionImagen.png"></p>

<strong>Imagen ya cargada dentro de la aplicación de Docker.</strong>

<p align="center"><img align="center" height="300" alt="image" src="./imagenes/ImagenCreada.png"></p>

<strong>Imagen por dentro.</strong>

<p align="center"><img align="center" height="300" alt="image" src="./imagenes/ImagenPorDentro.png"></p>

# Planeación Kubernertes

Kubernetes es una plataforma portable y extensible de código abierto para administrar cargas de trabajo y servicios. Kubernetes facilita la automatización y la configuración declarativa. Tiene un ecosistema grande y en rápido crecimiento.

Es hora de generar un cluster con Kubernetes. En este caso con ayuda de digitalocean estaríamos creando nuestro cluster, para esto ingresamos a la página de ellos y seleccionaríamos el tipo de cluster que necesitáramos.

<p align="center"><img align="center" height="100" alt="image" src="./imagenes/Istio/Imagen1.png"></p>

Se generaría una serie claves y documentos, los cuales se tendrían que agregar a nuestro proyecto.

<p align="center"><img align="center" height="150" alt="image" src="./imagenes/Istio/Imagen2.png"></p>

Y lo configuramos.

<p align="center"><img align="center" height="150" alt="image" src="./imagenes/Istio/Imagen3.png"></p>

revisaríamos los nodos.

<p align="center"><img height="25" alt="image" src="./imagenes/Istio/Imagen4.png"></p>

<p align="center"><img height="40" alt="image" src="./imagenes/Istio/Imagen5.png"></p>

Creamos el archivo de nuestro despliegue.

<p align="center"><img align="center" height="25" alt="image" src="./imagenes/Istio/Imagen6.png"></p>

Guardamos el archivo y aplicamos nuestro despliegue.

<p align="center"><img align="center" height="40" alt="image" src="./imagenes/Istio/Imagen7.png"></p>

Creamos el servicio. Primero creamos el archivo. 

<p align="center"><img align="center" height="100" alt="image" src="./imagenes/Istio/Imagen8.png"></p>

Establecemos todos estos parámetros de versión, tipo que sería parecido al archivo para el despliegue, también la metadata la configuración del selector, puerto.

<p align="center"><img align="center" height="25" alt="image" src="./imagenes/Istio/Imagen9.png"></p>

Y corremos el archivo para aplicar el servicio. 

<p align="center"><img align="center" height="300" alt="image" src="./imagenes/Istio/Imagen10.png"></p>

Consultamos el servicio.

<p align="center"><img align="center" height="25" alt="image" src="./imagenes/Istio/Imagen11.png"></p>

Tendríamos la muestra de nuestro servicio ya ejecutado.

<p align="center"><img align="center" height="200" alt="image" src="./imagenes/Istio/Imagen12.png"></p>

# Planeación Istio

Istio es una malla de servicios (es decir, una capa de redes de servicios modernizada) que ofrece una manera transparente e independiente de cualquier lenguaje de automatizar las funciones de red de una aplicación de forma flexible y sencilla.

El primer paso es generar a la instalación de Istio en nuestro clúster.

<p align="center"><img align="center" height="75" alt="image" src="./imagenes/Istio/Imagen1.png"></p>

Se generará la descarga los manifiestos en nuestros clústeres.

<p align="center"><img align="center" height="100" alt="image" src="./imagenes/Istio/Imagen2.png"></p> 

Ya con esto tendríamos a Istio corriendo.

<p align="center"><img align="center" height="150" alt="image" src="./imagenes/Istio/Imagen3.png"></p>

Es hora de correr los ejemplos, en este caso usaríamos 2 ejemplos de pequeñas apps, que se alojan en puertos.

<p align="center"><img align="center" height="25" alt="image" src="./imagenes/Istio/Imagen4.png"></p>

<p align="center"><img align="center" height="25" alt="image" src="./imagenes/Istio/Imagen5.png"></p>

Se crea el servicio. Hacemos lo mismo con la nueva app.

<p align="center"><img align="center" height="25" alt="image" src="./imagenes/Istio/Imagen6.png"></p>

<p align="center"><img align="center" height="25" alt="image" src="./imagenes/Istio/Imagen7.png"></p>

Y podemos revisar los pods, para ver los servicios desplegados.

<p align="center"><img align="center" height="100" alt="image" src="./imagenes/Istio/Imagen8.png"></p>

Lo que podemos analizar sobre este mismos es que ya se están ingresando 2 contenedores en cada pod.

<p align="center"><img align="center" height="50" alt="image" src="./imagenes/Istio/Imagen9.png"></p>

## Kiali

En este punto ya esta funcionando Istio, pero de igual manera lo que podemos hacer es generar un dashboard, que ya viene con Istio, el cual tiene el nombre de kiali. Usamos el comando:

<p align="center"><img align="center" height="250" alt="image" src="./imagenes/Istio/Imagen10.png"></p>

Nos abrirá una pestaña en nuestro navegador con el entorno.

<p align="center"><img align="center" height="25" alt="image" src="./imagenes/Istio/Imagen11.png"></p>

Para poder demostrar el tramifico de los pods, vamos a ingresar un while a una de las apps.

<p align="center"><img align="center" height="250" alt="image" src="./imagenes/Istio/Imagen12.png"></p>

Y nos empezara a detectar el tráfico.

También tenemos la posibilidad de llevar las estadísticas que obtenemos, llevarla con grafana.

<p align="center"><img align="center" height="250" alt="image" src="./imagenes/Istio/Imagen13.png"></p>

Y nos mostraría un gráfico de nuestros servicios.

# Bibliografía
<ul>
 <li>Rad, B. B., Bhatti, H. J., & Ahmadi, M. (2017). An introduction to docker and analysis of its performance. International Journal of Computer Science and Network Security (IJCSNS), 17(3), 228.</li>
 <li>Morales Tapias, C. C. (2022). Despliegue y gestión de microservicios usando Istio.</li>
 <li>Nogués García, J. (2018). Orquestación de contenedores con Kubernetes (Bachelor's thesis).</li>
 <ul>
 
 # Link video
 
https://www.youtube.com/watch?v=eWT51uPJbFI


