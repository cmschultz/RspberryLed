import RPi.GPIO as GPIO         #Importa a biblioteca das GPIO

                                #Importa a biblioteca de tempo

GPIO.setmode(GPIO.BOARD)   #Configura o modo de definição de pinos como BOARD (contagem de pinos da placa)

GPIO.setwarnings(False)           #Desativa os avisos 

GPIO.setup(7, GPIO.OUT)       #Configura o pino 18 da placa (GPIO24) como saída

while(1):                                   #Inicia o loop infinito

    print("LED ACESO\n")          #Escreve na Python Shell a mensagem "LED ACESO" e pula uma linha

    GPIO.output(7, 1)               #Coloca o pino 18 em nível alto (1)

    time.sleep(1)                        #Delay de 1 segundo

    print("LED APAGADO\n")      #Escreve na Python Shell a mensagem "LED APAGADO" e pula uma linha

    GPIO.output(7, 0)               #Coloca o pino 18 em nível baixo (0)

    time.sleep(1)                        #Delay de 1 segundo

