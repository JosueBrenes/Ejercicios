horasSemanales = int(input("Digite las cantidad de horas semanales trabajadas: "))

precioHora = int(input("Digite el precio que se le paga por hora: "))

horasMes = (horasSemanales * 4.2) # = Horas trabajadas por mes (mes cuenta con 4.2 semanas)

salario = (horasMes * precioHora) # = Multiplicamos horas trabajadas por mes y precio que pagan por hora para sacar el salario

cargosSociales = ((salario * 10.5) / 100)  # = Para sacar el 10.5% del salario se multiplica por 10.5 y se divide entre 100

asociacionSolidarista = ((salario * 5) / 100) # = Para sacar el 5% del salario se multiplica por 5 y se divide entre 100

deducciones = (cargosSociales + asociacionSolidarista) # = Una vez con esto se suman los resultados para ver el total de las deducciones

salarioNeto = (salario - deducciones) # = Se resta las deducciones con el salario para tener el salario neto (salario neto es con las rebajas del 10.5% y 5%)

print("Su salario mesual es de: " + str(salarioNeto)) 