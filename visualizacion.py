##Imports------------------------
import configuracion
import cola
import RS
import sumador
import multiplicador
import common_data_bus
##-------------------------------

def exe():
	print("Ciclo de Reloj: ", configuracion.clk)

	if configuracion.stall["general"] == 1:
		print("Stall")

	#Cola de instrucciones
	print("Instrucción en cola :", cola.operand, cola.dest, cola.vj, cola.vk)

	#sumador reservation station
	for i in range(configuracion.RS_sum):
		if configuracion.registro_en_uso[i] == 1:
			b = 0
		else:
			b = 1
		print("RS_sumador", i,  "Bit de validez : ", b, " | Registro de destino : ", RS.dsum[i], " | Realizando : ", RS.rsum[i], " | Valor 1 : ", RS.sum1[i], " | Valor 2 : ", RS.sum2[i])

	#multiplicador reservation station
	for i in range(configuracion.RS_mul):
		if configuracion.registro_en_uso[i] == 1:
			c = 0
		else:
			c = 1
		print("RS_mul", i,  "Bit de validez : ", c, " | Registro de destino : ", RS.dmul[i], " | Realizando : ", RS.rmul[i], " | Valor 1 : ", RS.mul1[i], " | Valor 2 : ", RS.mul2[i])

	#If sumador starts a calculation or is done with it
	for i in range(configuracion.RS_sum):
		if sumador.start_add[i] == 1 and configuracion.clk == sumador.start_clk_add[i]:
			print("Sumador", i, " ha iniciado la operación : ", sumador.op_add[i], sumador.add1[i], sumador.add2[i], " | Registro de destino : ", sumador.dsum[i], " enviado en CDB")

		if sumador.start_clk_add[i] != 0 and configuracion.clk == (sumador.start_clk_add[i] + configuracion.ciclos_sum):
	 		print("Sumador", i, " ha iniciado la operación : ", sumador.op_add[i], sumador.add1[i], sumador.add2[i], " | Registro de destino : ", sumador.dsum[i], " enviado en CDB")

	 #If multiplicador starts a calculation or is done with it
	for i in range(configuracion.RS_mul):
		if multiplicador.start_mul[i] == 1 and configuracion.clk == multiplicador.start_clk_mul[i]:
			print("Multiplicador", i, " ha iniciado la operación : ", multiplicador.op_mul[i], multiplicador.mul1[i], multiplicador.mul2[i], " | Registro de destino : ", multiplicador.dmul[i], "enviado en CDB")

		if multiplicador.start_clk_mul[i] != 0 and configuracion.clk == (multiplicador.start_clk_mul[i] + configuracion.ciclos_mul):
	 		print("Multiplicador", i, " ha iniciado la operación : ", multiplicador.op_mul[i], multiplicador.mul1[i], multiplicador.mul2[i], " | Registro de destino : ", multiplicador.dmul[i], "enviado en CDB")

	# Registros
	for i in range(len(configuracion.registro)):
		if configuracion.registro_en_uso[i] == 1:
			a = 0
		else:
			a = 1

		print("R", i, ": ", configuracion.registro[i], " | Bit de validez ", i, ": ", a, sep='')
	

	print()