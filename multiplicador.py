import configuracion

global start_clk_mul, mul1, mul2, op_mul, busy_mul, start_mul, dmul
start_clk_mul = [0]*configuracion.RS_mul
mul1 = [0]*configuracion.RS_mul
mul2 = [0]*configuracion.RS_mul
op_mul = [0]*configuracion.RS_mul
busy_mul = [0]*configuracion.RS_mul
start_mul = [0]*configuracion.RS_mul
dmul = ['00']*configuracion.RS_mul

def exe(number, op, v1, v2, dest):
	
	if op == "MUL": #Revisa si es una multiplicación
		op_mul[number] = op
		mul1[number] = v1
		mul2[number] = v2
		dmul[number] = dest
		start_clk_mul[number] = configuracion.clk
		start_mul[number] = 1

	elif op == 0 and configuracion.clk == start_clk_mul[number] + configuracion.ciclos_mul and start_clk_mul[number] != 0: #Envía el resultado en el CDB cuando termina la ejecución
		if op_mul[number] == "MUL":
			configuracion.cola_de_resultados.append([dmul[number], mul1[number] * mul2[number]])
		
		busy_mul[number] = 0 #El multiplicador se desocupa
		start_mul[number] = 0