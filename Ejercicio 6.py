dias = int(input("Digite los dias que va a la universidad por semana: ")) 

km = int(input("Digite la distancia en km de su casa a la universidad: ")) 

costo = int(input("Digite el costo por km para trasladarse: ")) 

totalDias = (15 * dias) 

totalCosto = (km * 2) * costo 

totalCuatri = (totalDias * totalCosto)

print("El total de trasladarse por cuatrimestre a la U es de: " + str(totalCuatri))