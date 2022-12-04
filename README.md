# Tolerancia Fallas
Este proyecto trata de un BOT que se gestiona por medio de una API de Telegram, todo por medio de de un mismo CHAT de telegram y tener una escalabilidad para al mmismo
y tolerancia a fallas, algunas de las herramientas que se utilizamos fueron Docker, Kubernetes, Istio y por supuesto GitHub.

<img height="100" alt="image" src="./imagenes/GitHub.jpg"><img height="100" alt="image" src="./imagenes/docker.png"><img height="100" alt="image" src="./imagenes/kubernetes.png"><img height="100" alt="image" src="./imagenes/istio.png">

# Introducción
 Para este proyecto usamos algunas herramientas que aprendimos en nuestro curso de tolerancia a fallas, e implementamos una herrmientas que que descubrimos durante el curso la cual es el <strong>WebScraping</strong> esta es una librería que podemos encontrar en el lenguaje de programación de <i><strong>Python</strong></i>, es una técnica que sirve para extraer información de uno o varios sitios webs de terceros.
 Tambien hacemos uso de una API de telegram que nos permite enlazar enviar notifacaciones al usuario en cuestión. Todo esto por supuesto escalandolo a contenedores,  llevandolo a otros servidores y a monitoriar el trafico entre ellos.
# Requerimientos
<i><ul>
  <li>Python: 3.10.8
  	<ul><b>Librerías</b>
  		<li>beautifulsoup4: 4.11.1</li>
  		<li>request: 2.28.1</li>
  		<li>webroser</li>
  	</ul>
  </li>
 
 # Web Scraping
 En primera instancia lo que hacemos es conseguir los datos de la página web para poder trabajas con ellos, en este caso solo con el dato que requierimos el cual es el precio del producto, es muy sencillo el generar la lectura en este caso para el programa solo es necesario identificar un objeto, para este caso es necesario indicar al programa cual objeto de <i>HTML</i> es el que nos interesa. 

 <img height="300" alt="image" src="./imagenes/mercadoLibreModoProgramador.png">
