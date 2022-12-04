# Tolerancia Fallas
Este proyecto trata de un BOT que se gestiona por medio de una API de Telegram, todo por medio de de un mismo CHAT de telegram y tener una escalabilidad para al mmismo
y tolerancia a fallas, algunas de las herramientas que se utilizamos fueron Docker, Kubernetes, Istio y por supuesto GitHub.

<img width="200" alt="image" src="./imagenes/GitHub.png">
<img width="200" alt="image" src="./imagenes/docker.png">
<img width="200" alt="image" src="./imagenes/kubernetes.png">
<img width="200" alt="image" src="./imagenes/istio.png">

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
