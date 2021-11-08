import configuracion

global start_clk_add, add1, add2, op_add, busy_add, start_add, dsum
start_clk_add = [0]*configuracion.RS_sum
add1 = [0]*configuracion.RS_sum
add2 = [0]*configuracion.RS_sum
op_add = [0]*configuracion.RS_sum
busy_add = [0]*configuracion.RS_sum
start_add = [0]*configuracion.RS_sum
dsum = ['00']*configuracion.RS_sum

def exe(number, op, v1, v2, dest):
	
	if op == "ADD" or op == "SUB": #Revisa instrucción
		op_add[number] = op
		add1[number] = v1
		add2[number] = v2
		dsum[number] = dest
		start_clk_add[number] = configuracion.clk
		start_add[number] = 1

	elif op == 0 and configuracion.clk == start_clk_add[number] + configuracion.ciclos_sum and start_clk_add[number] != 0: #Envía el resultado en el CDB cuando termina la ejecución
		if op_add[number] == "ADD":
			configuracion.cola_de_resultados.append([dsum[number], add1[number] + add2[number]])
			
		elif op_add[number] == "SUB":
			configuracion.result_queue.append([dsum[number], add1[number] - add2[number]])

		busy_add[number] = 0 #Sumador ya no está ocupado
		start_add[number] = 0