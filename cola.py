import configuracion
import sumador

issue_stall = 0

def exe():
	global instruction, operand, dest, vj, vk, issue_stall

	if configuracion.stall["issue"] == 0 and configuracion.stall["add"] == 0 and configuracion.stall["mul"] == 0 and configuracion.clk != 1 and len(configuracion.cola_de_instrucciones) != 0: #Si no se encuentra otra instruccion de stall proveniente de un bloque , el fetch y decode  de instrucciones no se detiene y puede eliminar la ultima instruccion de la cola
		configuracion.cola_de_instrucciones.pop(0)																																				
		configuracion.stall["general"] = 0

	if len(configuracion.cola_de_instrucciones) == 0: # Ocurre cuando no hay mas instrucciones que procesar
		return 0, 0, 0, 0

	## Decodificando la prixima instruccion y eliminandola de la cola
	instruction = configuracion.cola_de_instrucciones[0].split()
	operand = instruction[0]
	dest = instruction[1]
	vj = instruction[2]
	vk = instruction[3]


	if configuracion.registro_en_uso[int(dest[1])] == 1: # Si el registro de destino esta siendo utilizado , hace us tall a la insrtuccion que se esta emitiendo
		configuracion.stall["issue"] = 1
		operand = 0
		dest = 0
		vj = 0
		vk = 0

	else:
		configuracion.stall["issue"] = 0

	if configuracion.stall["issue"] == 1  or configuracion.stall["add"] == 1 or configuracion.stall["mul"] == 1: ## Revisa si hay algun stall proveniente de algun bloque
		configuracion.stall["general"] = 1

	else: ##Si no se cumple la condicion previa la instruccion puede ser emitida
		configuracion.instruction_issued = 0
	
	return operand, dest, vj, vk

	# else:
	# 	print("return 0")
	# 	return 0, 0, 0, 0



	