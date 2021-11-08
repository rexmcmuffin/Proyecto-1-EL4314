import configuracion
from RS import sum1, sum2, mul1, mul2

global registro

def exe():

	# Realiza fetch en los resultados en la cola_de_resultados y los envía de nuevo a los registros y RS's
	for i in range(len(configuracion.cola_de_resultados)):
		result = configuracion.cola_de_resultados[0]
		reg_num = int((result[0])[1:])
		configuracion.registro[reg_num] = result[1] #Almacena el resultado en el registro
		configuracion.registro_en_uso[reg_num] = 0

		for j in range(configuracion.RS_sum): #Revisa si RS de suma requiere los resultados
			if sum1[j] == result[0]:
				sum1[j] = result[1]
				
			if sum2[j] == result[0]:
				sum2[j] = result[1]
				
		for j in range(configuracion.RS_mul): #Revisa si RS de suma requiere los resultados
			if mul1[j] == result[0]:
				mul1[j] = result[1]
				
			if mul2[j] == result[0]:
				mul2[j] = result[1]

		configuracion.cola_de_resultados.pop(0)