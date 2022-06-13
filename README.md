# Tarea 3

## Integrantes

Santiago Morales - 17624541

Ignacio Winter - 17642329

## Simulacion

### Parte 1: paquete Simple PDU

1. ¿Cual es el largo en bits de la direccion IP de destino?

* La direccion IP de destino, que corresponde a 200.0.0.2, tiene un largo de 32 bits.

2. ¿Cual es la direccion IP de origen cuando el paquete se encuentra en el router central y el ultimo dispositivo visitado es el router gateway de la red Casa Manolito?

* La direccion Ip de origen en la situacion descrita corresponde a la 111.11.11.2 

3. ¿Cual es la direccion IP de origen cuando el paquete se encuentra en el router central y el ultimo dispositivo visitado es el router gateway de la red DNS?

* La direccion Ip de origen en la situacion descrita corresponde a la 200.0.0.2

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
