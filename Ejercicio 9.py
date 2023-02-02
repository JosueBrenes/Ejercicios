# = Le solicitamos al usuario sus ingresos mensuales
print("Digite sus ingresos mensuales")
ingresos = input()
ingresos = int(ingresos)

# = Le solicitamos cuanto gasta mensualmente en alimentacion
print("Digite sus gastos mensuales en alimentacion")
gastos = input()
gastos = int(gastos)

# = Ahora sacamos el porcentaje correspondiente al rubro de alimentacion 
total = ((gastos * 100) // ingresos)

# = Imprimimos el resultado correspondiente
print("El gasto correspondiente al rubro de alimentacion es de: " + str(total) + "%")

# = Calculamos cuanto le queda para otros rubros que es el 100% - total
restante = (100 - total)

# = Imprimimos el resultado correspondiente
print("El porcentaje disponible para otros rubros es de " + str(restante) + "%")