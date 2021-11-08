# Proyecto-1-EL4314
Proyecto 1 Arquitectura de computadores - Simulador del algoritmo Tomasulo

Integrantes:

David Felipe Duarte Sanchez
Wanderley Cortés Morales
CJM

Requisitos del proyecto:

El simulador debe de ser capaz de recibir como entrada un archivo de texto el cual contiene el codigo a ejecutar
se utiliza el siguiente codigo como ejemplo:


mul r3, r1, r2
add r5, r3, r4
add r7, r2, r6
add r10, r8, r9
mul r11, r7, r10
add r5, r5, r11

Siguiente a esto el simulador solamente tomara en cuenta instrucciones del tipo add, sub y mul, las mismas 
requieren los siguientes ciclos de reloj:

add -> 4
sub -> 4
mul -> 6

El simulador cuenta con dos estaciones de reserva (RS), una para add y sub y la otra para mul. El tamaño de estas 
RS (cantidad de instrucciones almacenables) sera configurable en el menu del simulador. Cada entrada de la RS debe
de tener informacion correspondiente a las fuentes, etiqueta, valor y validez.

La tabla de alias de registro (RAT) tendra capacidad para 12 registros, de r1 a r12, los mismos deben de contener el
nombre del registro, la validez de su contenido, la etiqueta con la cual es renombrado y el valor del registro.

Cada vez que se completa el ultimo ciclo de reloj de la ejecucion de una instruccion en una unidad funcional, el resultado
se difunde tanto al aRAT, para actualizar los registros como a los RS para actualizar las fuentes de las operaciones que estan
en espera.

En todo momento el simulador debe de indicar al usuario el estado de ejecucion de las instrucciones la RAT y las RS , de manera
que permita conocer el avance del programa. Una vez finalizada la simulacion se debe de indicar la cantidad de ciclos de reloj
utilizados para ejecutar el programa 
