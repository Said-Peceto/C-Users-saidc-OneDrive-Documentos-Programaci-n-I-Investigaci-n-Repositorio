"""programa dos, es un programa que recopila información personal del usuario y es simple. aqui utilize el .lower() para que lo que escriba sean
en miniscula"""

print("¡Bienvenido a nuestro programa de recopilación de datos personales!")
nombre = input("Por favor, ingresa tu nombre completo: ")
edad = input("¿Cuál es tu edad? ")
genero = input("¿Eres hombre o mujer? ")

if genero.lower() == "hombre":
    print("Hola, Sr. " + nombre)
elif genero.lower() == "mujer":
    print("Hola, Sra. " + nombre)
else:
    print("Hola, " + nombre)

if int(edad) < 18:
    print("Eres menor de edad")
else:
    print("Eres mayor de edad")

estado_civil = input("¿Cuál es tu estado civil? (Soltero/Casado/Divorciado/Viudo) ")
if estado_civil.lower() == "soltero":
    print("Interesante, eres soltero.")
elif estado_civil.lower() == "casado":
    print("¡Felicitaciones por tu matrimonio!")
elif estado_civil.lower() == "divorciado":
    print("Lo siento por tu divorcio.")
elif estado_civil.lower() == "viudo":
    print("Lo siento por tu pérdida.")
else:
    print("No reconocemos ese estado civil.")
