##Imports------------------------
import time
import visualizacion
import configuracion
import cola
import RS
import sumador
import multiplicador
import common_data_bus
#-------------------------------

configuracion.init() #Inicializa la configuracion segun configuracion.py

#Loop principal
i=0
b=0

while (1 in configuracion.registro_en_uso or b==0):
	b=1
	instruction = cola.exe() #Fetch y decode

	for i in range(configuracion.RS_sum): #Envía instrucción a RS de suma
		RS.add_exe(i, instruction)
		sumador.exe(i, 0, 0, 0, 0)

	for i in range(configuracion.RS_mul): #Envía instrucción a RS de multiplicación
		RS.mul_exe(i, instruction)
		multiplicador.exe(i, 0, 0, 0, 0)


	common_data_bus.exe() #EL Common Data Bus, permite emitir el resultado de vuelta a los registros y RS's

	visualizacion.exe() #Permite visualizar los datos en la terminal
	
	time.sleep(configuracion.delay) #Delay
	configuracion.clk=configuracion.clk+1    #Pasa a siguiente ciclo de reloj
	i=i+1


