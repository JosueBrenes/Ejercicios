print("Digite la edad de la persona A: ")
a = input()
a = int(a)

print("Digite la edad de la persona B: ")
b = input()
b = int(b)

print("Digite la edad de la persona C: ")
c = input()
c = int(c)

print("Digite la edad de la persona D: ")
d = input()
d = int(d)

print("Digite la edad de la persona E: ")
e = input()
e = int(e)

edad = ((a + b + c + d + e) // 5)
print("La edad promedio es de: " + str(edad))