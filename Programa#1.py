#Programa Uno, es un programa que recomienda un producto basado en las preferencias del usuario
# Preguntar las preferencias del usuario
print("¡Bienvenido a nuestro sistema de recomendación!")
print("Por favor, conteste las siguientes preguntas para poder recomendarle un producto.")
print()

preferencia_color = input("¿Cuál es su color favorito? ")
preferencia_categoria = input("¿Prefiere productos electrónicos o de moda? ")
preferencia_precio = int(input("¿Cuál es su presupuesto máximo en dólares? "))

# Recomendar un producto basado en las preferencias del usuario
if preferencia_color == "azul" and preferencia_categoria == "electrónicos" and preferencia_precio >= 500:
    print("Le recomendamos la computadora portátil XYZ. Es de color azul, tiene características de última generación y está dentro de su presupuesto.")
elif preferencia_color == "rojo" and preferencia_categoria == "moda" and preferencia_precio >= 50:
    print("Le recomendamos el vestido ABC. Es de color rojo, está a la moda y tiene un buen precio.")
elif preferencia_categoria == "electrónicos" and preferencia_precio >= 100:
    print("Le recomendamos los audífonos Bluetooth DEF. Tienen una gran calidad de sonido y están dentro de su presupuesto.")
else:
    print("Lo siento, no podemos recomendarle un producto en este momento.")