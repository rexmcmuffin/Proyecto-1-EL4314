## Contiene las configuraciones para el funcionamiento del algoritmo

global RS_sum  #Tamaño de RS's
RS_sum = 3

global RS_mul
RS_mul = 2

def init():
	global clk  #Reloj
	clk = 1

	global delay 
	delay = 1

	global registro 
	registro = [1,2,3,4,5,6,7,8,9,10,11,12]
	global registro_en_uso
	registro_en_uso = [0,0,0,0,0,0,0,0,0,0,0,0]

	global stall
	stall = { "general": 0,
  			  "issue": 0,
  			  "add": 0,
  			  "mul": 0 }

	global cola_de_instrucciones
	cola_de_instrucciones=[]
	non_wanted_characters="\,n"
	with open("codigo_de_entrada.txt") as f:
		lines = f.readlines()
		for count in lines :
			string=count
			for x in range(len(non_wanted_characters)):
				string=string.replace(non_wanted_characters[x],"")
				string=string.rstrip('\n')
			cola_de_instrucciones.append(string)
	#print(cola_de_instrucciones)
	#cola_de_instrucciones = ['MUL R2 R0 R1', 'ADD R4 R2 R3', 'ADD R6 R1 R5', 'ADD R9 R7 R8', 'MUL R10 R6 R9', 'ADD R4 R4 R10']

	global cola_de_resultados
	cola_de_resultados = [[] for i in range(12)]
	cola_de_resultados.clear()

	global ciclos_sum
	ciclos_sum = 4


	global ciclos_mul
	ciclos_mul = 6

	global RAT
	RAT = 12




