"""programa tres, es un programa que te pide responder una serie de preguntas para determinar tus gustos musicales, solamente define el posible
gusto musical que se relaciona a tu respuesta del cuestionario"""

print("¡Bienvenido al cuestionario de gustos musicales!")
print("Responde las siguientes preguntas para recomendarte un género musical.")

respuesta1 = input("¿Te gusta más la música suave y relajante o la música enérgica y movida? ")
if respuesta1 == "suave":
    respuesta2 = input("¿Prefieres la música instrumental o con voces? ")
    if respuesta2 == "instrumental":
        print("Te recomendamos el género musical de la música clásica.")
    elif respuesta2 == "voces":
        print("Te recomendamos el género musical del jazz.")
    else:
        print("Lo siento, no entendí tu respuesta.")
elif respuesta1 == "movida":
    respuesta2 = input("¿Te gusta más la música con instrumentos de cuerda o de viento? ")
    if respuesta2 == "cuerda":
        print("Te recomendamos el género musical del rock.")
    elif respuesta2 == "viento":
        print("Te recomendamos el género musical del blues.")
    else:
        print("Lo siento, no entendí tu respuesta.")
else:
    print("Lo siento, no entendí tu respuesta.")
