import configuracion
import sumador
import multiplicador

global rsum, sum1, sum2, dsum 

rsum = [0]*configuracion.RS_sum
sum1 = [0]*configuracion.RS_sum
sum2 = [0]*configuracion.RS_sum
dsum = [0]*configuracion.RS_sum

def add_exe(number, instruction):


	if sumador.busy_add[number] == 1 and sumador.start_add[number] == 0:  #Si la instrucción se registró por RS, pero aún no inicia su ejecución porque falta un dato
		if isinstance(sum1[number], int) and isinstance(sum2[number], int):  #Revisa si ya se tienen todos los datos necesarios, de ser así realiza la suma
			sumador.exe(number, rsum[number], sum1[number], sum2[number], dsum[number])


	if sumador.busy_add[number] == 0 and (instruction[0] == "ADD" or instruction[0] == "SUB") and configuracion.instruction_issued == 0: #Si se recibe la instrucción y RS aún no está ocupada
		sumador.busy_add[number] = 1  #Marca la RS como ocupada y mantiene la instrucción 
		rsum[number] = instruction[0]
		dsum[number] = instruction[1]
		configuracion.registro_en_uso[int(dsum[number][1:])] = 1
		sum1[number] = instruction[2]
		sum2[number] = instruction[3]

		if(sum1[number][0] != 'R'): #Para operandos inmediatos
			sum1[number] = int(sum1[number])	
		else: # Sino se revisa si el registro deseado tiene un valor y no se está ocupando
			reg_number = int(sum1[number][1:])
			if configuracion.registro_en_uso[reg_number] == 0: 
				sum1[number] = configuracion.registro[reg_number]

			if (configuracion.registro_en_uso[reg_number] == 1 and dsum[number] == sum1[number]) or (configuracion.registro_en_uso[reg_number] == 1 and dsum[number] == sum2[number]):
				sum1[number] = configuracion.registro[reg_number]

		if(sum2[number][0] != 'R'): #Lo misma para el segundo valor
			sum2[number] = int(sum2[number])
		else:
			reg_number = int(sum2[number][1:])
			if configuracion.registro_en_uso[reg_number] == 0: 
				sum2[number] = configuracion.registro[reg_number]
			if (configuracion.registro_en_uso[reg_number] == 1 and dsum[number] == sum1[number]) or (configuracion.registro_en_uso[reg_number] == 1 and dsum[number] == sum2[number]):
				sum2[number] = configuracion.registro[reg_number]
		configuracion.instruction_issued = 1 #Instrucción registrada por RS
		configuracion.stall["add"] = 0

	if number == configuracion.RS_sum-1 and configuracion.instruction_issued == 0 and (instruction[0] == "ADD" or instruction[0] == "SUB"): #Stall si RS están llenas
		configuracion.stall["add"] = 1


#Se tiene lo mismo para el caso de la multiplicación

global rmul, mul1, mul2, dmul

rmul = [0]*configuracion.RS_mul
mul1 = [0]*configuracion.RS_mul
mul2 = [0]*configuracion.RS_mul
dmul = [0]*configuracion.RS_mul

	
def mul_exe(number, instruction):

	if multiplicador.busy_mul[number] == 1 and multiplicador.start_mul[number] == 0:
		if isinstance(mul1[number], int) and isinstance(mul2[number], int):
			multiplicador.exe(number, rmul[number], mul1[number], mul2[number], dmul[number])

	if multiplicador.busy_mul[number] == 0 and (instruction[0] == "MUL") and configuracion.instruction_issued == 0:

		multiplicador.busy_mul[number] = 1
		rmul[number] = instruction[0]
		dmul[number] = instruction[1]
		configuracion.registro_en_uso[int(dmul[number][1:])] = 1
		mul1[number] = instruction[2]
		mul2[number] = instruction[3]

		if(mul1[number][0] != 'R'):
			mul1[number] = int(mul1[number])	
		else:
			reg_number = int(mul1[number][1:])
			if configuracion.registro_en_uso[reg_number] == 0 :
				mul1[number] = configuracion.registro[reg_number]

			if (configuracion.registro_en_uso[reg_number] == 1 and dmul[number] == mul1[number]) or (configuracion.registro_en_uso[reg_number] == 1 and dmul[number] == mul2[number]):
				mul1[number] = configuracion.registro[reg_number]
				

		if(mul2[number][0] != 'R'):
			mul2[number] = int(mul2[number])
		else:
			reg_number = int(mul2[number][1:])
			if configuracion.registro_en_uso[reg_number] == 0 : 
				mul2[number] = configuracion.registro[reg_number]

			if (configuracion.registro_en_uso[reg_number] == 1 and dmul[number] == mul1[number]) or (configuracion.registro_en_uso[reg_number] == 1 and dmul[number] == mul2[number]):
				mul2[number] = configuracion.registro[reg_number]

		configuracion.instruction_issued = 1
		configuracion.stall["mul"] = 0

	if number == configuracion.RS_sum-1 and configuracion.instruction_issued == 0 and (instruction[0] == "MUL"):
		configuracion.stall["mul"] = 1