print("Digite sus ingresos mensuales")
ingresos = input()
ingresos = int(ingresos)

print("Digite sus gastos mensuales en alimentacion")
gastos = input()
gastos = int(gastos)

total = ((gastos * 100) // ingresos)
print("El gasto correspondiente al rubro de alimentacion es de: " + str(total) + "%")

restante = (100 - total)
print("El porcentaje disponible para otros rubros es de " + str(restante) + "%")
  
#Prueba