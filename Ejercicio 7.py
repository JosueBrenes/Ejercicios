# = Le solicitamos la edad de la persona A
print("Digite la edad de la persona A: ")
a = input()
a = int(a)

# = Le solicitamos la edad de la persona B
print("Digite la edad de la persona B: ")
b = input()
b = int(b)

# = Le solicitamos la edad de la persona C
print("Digite la edad de la persona C: ")
c = input()
c = int(c)

# = Le solicitamos la edad de la persona D
print("Digite la edad de la persona D: ")
d = input()
d = int(d)

# = Le solicitamos la edad de la persona E
print("Digite la edad de la persona E: ")
e = input()
e = int(e)

# = Se suman las edades de todos y se divide entre 5 ya que son 5 personas 
edad = ((a + b + c + d + e) // 5)

# = Imprimimos el resultado que es la edad primedio
print("La edad promedio es de: " + str(edad))