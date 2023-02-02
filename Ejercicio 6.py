# = Le solicitamos los dias que va a la universidad
print("Digite los dias que va a la universidad: ")
dias = input()
dias = int(dias)

# = le solicitamos la distancia en km de la casa a la universidad
print("Digite la distancia en km de su casa a la universidad: ")
km = input()
km = int(km)

# = Le solicitamos el costo por km para trasladarse
print("Digite el costo por km para trasladarse: ")
costo = input()
costo = int(costo)

# = Se calculan los dias que va a la U por cuatrimestre
totalDias = (15 * dias) 

# = Se calcula el costo ida y vuelta 
totalCosto = (km * 2) * costo 

# = Se multiplican los total dias por totalCosto para sacar el monto total que paga para trasladarse por cuatrimentre
totalCuatri = (totalDias * totalCosto)

# = Imprimimos el resultado obtenido 
print("El total de trasladarse por cuatrimestre a la U es de: " + str(totalCuatri))