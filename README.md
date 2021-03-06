# Tarea 3

## Integrantes

Santiago Morales - 17624541

Ignacio Winter - 17642329

## Simulacion

### Parte 1: paquete Simple PDU

1. ¿Cual es el largo en bits de la direccion IP de destino?

* La direccion IP de destino, que corresponde a 200.0.0.2, tiene un largo de 32 bits.

2. ¿Cual es la direccion IP de origen cuando el paquete se encuentra en el router central y el ultimo dispositivo visitado es el router gateway de la red Casa Manolito?

* La direccion IP de origen en la situacion descrita corresponde a la 111.11.11.2 

3. ¿Cual es la direccion IP de origen cuando el paquete se encuentra en el router central y el ultimo dispositivo visitado es el router gateway de la red DNS?

* La direccion IP de origen en la situacion descrita corresponde a la 200.0.0.2

4. Describa, en orden y separado por capas de entrada y salida, todo lo que ocurre con el paquete cuando este se encuentra en el servidor de la red DNS y el ultimo dispositivo visitado es el router gateway de la red DNS.

Capas de Entrada

* Layer 1: El puerto FastEthernet0 recibe el paquete enviado.

* Layer 2: La dirección MAC de destino del paquete concide con la direccion del puerto que lo recibe, con la de direccion de broadcast o con la direccion multicast. El dispositivo desencapsula el paquete simple PDU.

* Layer 3: La dirección IP de destino del paquete coincide con la dirección IP del dispositivo o la dirección de broadcast. El dispositivo desencapsula el paquete. Ya que el paquete PDU corresponde a un paquete ICMP, entonces es procesado mediante el proceso ICMP. El proceso ICMP recibe un mesnaje "Echo Request".

Capas de Salida

* Layer 1: El paquete es enviado afuera mediante el puerto FastEthernet0.

* Layer 2: La dirección IP del Next Hop es unicast. El proceso ARP busca la direccion en la tabla ARP. Es encontrado en la tabla, por lo que el proceso ARP fija la direccion MAC de destino segun lo que encontro en la tabla. El dispositivo encapsula el PDU en un paquete Ethernet.  

* Layer 3: El proceso ICMP responde a la "Echo Request" ajustando la la respuesta al tipo ICMP. Luego manda la respuesta. La direccion de destino 111.11.11.2 no es la misma sub red y no es la direccion de broadcast, por lo que el dispositivo establece el "default gateway" para el Next Hop.

### Parte 2

1. ¿Cual es el largo en bytes del HTTP Request del paquete HTTP?

* El HTTP Request del paquete HTTP tiene un largo de 32 bytes.

2. Describa que tipos de paquetes se estan usando, es decir, decir que tipo de paquete son, por que se usan estos paquetes y que deben contener.

* Se estan utilizando, en primer lugar, paquetes DNS, que sirven para traducir los nombres de dominio a la direccion IP del servidor donde esta la pagina a la que queremos acceder. Estos paquetes deben contener el nombre de la pagina web a la que se esta tratando de acceder, el IP de destino, el Time to Live, class y type. También se utiliza el Adress Resolution Protocol (ARP) que cumple la funcion de establecer una correspondencia entre la direccion IP y la direccion MAC (De esto ultimo no estoy seguro porque me aparecio solo en una sola simulacion). Por ultimo, se utiliza el paquete HTTP, que se manda primero con un HTTP Request y luego con un HTTP Response. El HTTP Request, enviadas por el cliente al servidor, se utilizan para pedir el inicio de una acción y contienen el metodo que describe la accion, los headers, una empty line y el body. El HTTP Response, que es la respuesta del servidor, tiene una estructura similar al Request, pero en la linea de inicio describe si la peticion tuvo exito o fracaso.  

3. Describa de forma ordenada que rutas toman los paquetes descritos en la pregunta anterior (especificar por donde pasan y en que orden).

* En primer lugar se envia un DNS desde la Laptop de la red Casa Manolito hacia el Router de la Casa, el cual a su vez envia el DNS hacia el Router Gateaway de esta red. Luego lleva este paquete a la Router Central. El paquete sigue el camino hacia el Router Gateaway de la red DNS para finalmente llegar al Server DNS. El paquete DNS hace el mismo camino de vuelta hacia el Laptop de la red Casa Manolito, llegando exitosamente. (Server DNS -> Router Gateaway red DNS -> Router Central -> Router Gateaway red Casa Manolito -> Router red Casa Manolito -> Laptop). Al llegar exitosamente el DNS al Laptop, este ultimo manda un HTTP Request al Server de la red Disney+, el cual hace el siguiente camino: Laptop red casa Manolito -> Router red Casa Manolito -> Router Gateaway red Casa Manolito -> Router Central -> Router Gateaway red Disney+ -> Server Disney+. El Server de Disney+, a su vez, envía un HTTP Response de vuelta al Latop siguiendo el camino exactamente en orden inverso. 
