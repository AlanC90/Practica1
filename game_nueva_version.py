from random import choice, randrange
from datetime import datetime
import string

#Inicio del programa.
print('--------------------\n')
print("Bienvenido/a.\n")

# Operadores posibles.
operators = ["+", "-", "*", "/"]
# Cantidad de cuentas a resolver.
times = 5
# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()

#Correctos, incorrectos, respuestas no validas y sin respuesta.
correctos = 0
incorrectos = 0
respNoValidas = 0
sinResp = 0    

#Para validar respuesta usuario.
digitos = string.digits
simbolos_aritmet = [",", ".", "+", "-" ]


print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!\n")

for i in range(0, times):    

    # Se eligen números y operador al azar.
    operator = choice(operators)
    number_1 = randrange(10)
    number_2 = randrange(10)
    
    #Para evitar division por cero.
    if operator == '/':
      while number_2 == 0:                  
        number_2 = randrange(10) 
    
    
    # Se imprime la cuenta.
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?\n")
    

    #Calculo de resultado.
    match operator:
        case "+":
            res = number_1 + number_2     
        case "-":
            res = number_1 - number_2                      
        case "*":
            res = number_1 * number_2                 
        case "/":               
            res = number_1 / number_2 
            #Acotar a 2 decimales.
              #Se convierte de float a string, se acota el string, y este se convierte luego a float.
            res = float(str(res)[0:4])            
                
                    
    # Le pedimos al usuario el resultado.
    if operator == '/':
        resUser = input("Resultado (hasta 2 digitos decimales): ")
    else:  
        resUser = input("Resultado: ")
        
    #Se procesa si hay respuesta.
    if resUser != "":        

        #Verificamos si es valida.            
        valida = True                       
        for elem in resUser:
            if elem not in digitos and elem not in simbolos_aritmet:
                valida = False
        
        if valida:       
            resUser = float(resUser)

            #Informamos en pantalla si fue correcto o no.
            if res == resUser:
                print("Correcto\n")
                correctos += 1
            else:
                print("Incorrecto\n")
                incorrectos += 1
        else:
                print("Respuesta no valida\n")
                respNoValidas += 1

    else:
        print("No se ingreso respuesta\n")
        sinResp += 1;                        

    print()

      
# Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time
# Mostramos ese tiempo en segundos.
print(f"\n Tardaste {total_time.seconds} segundos.")

# Informamos cantidad de aciertos y desaciertos.
print(f" Acertaste {correctos} veces. Te equivocaste {incorrectos} veces. Respuestas no válidas: {respNoValidas}. Sin responder: {sinResp}.\n")


#Fin del programa.
print()
print("Fin del programa.\n")
print("--------------------\n")

