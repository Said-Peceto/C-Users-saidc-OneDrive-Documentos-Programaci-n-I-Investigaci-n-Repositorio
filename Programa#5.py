""""Programa cinco, este programa te recomienda que producto comprar segun lo que quieres en el dia, ejemplo: hoy quiero comprar un producto
de belleza personal, lo que hace el programa es sugerirte que producto te recomendaria"""

# Preguntar al usuario sobre sus preferencias de compra
preferencia = input("¿Qué producto necesitas hoy? (alimentos, productos de limpieza, productos de belleza): ")

# Si el usuario selecciona alimentos
if preferencia == "alimentos":
    # Preguntar sobre la categoría de alimentos que necesita
    categoria = input("¿Qué tipo de alimentos necesitas? (frutas, verduras, carnes, lácteos): ")
    # Recomendar productos de la categoría seleccionada
    if categoria == "frutas":
        print("Podrías comprar manzanas, plátanos y peras.")
    elif categoria == "verduras":
        print("Podrías comprar lechuga, brócoli y zanahorias.")
    elif categoria == "carnes":
        print("Podrías comprar pollo, res y cerdo.")
    elif categoria == "lácteos":
        print("Podrías comprar leche, queso y yogurt.")

# Si el usuario selecciona productos de limpieza
elif preferencia == "productos de limpieza":
    # Preguntar sobre la categoría de productos de limpieza que necesita
    categoria = input("¿Qué tipo de productos de limpieza necesitas? (limpiadores, desinfectantes, detergentes): ")
    # Recomendar productos de la categoría seleccionada
    if categoria == "limpiadores":
        print("Podrías comprar limpiavidrios, limpiamuebles y limpia pisos.")
    elif categoria == "desinfectantes":
        print("Podrías comprar cloro, desinfectante multiusos y desinfectante de baño.")
    elif categoria == "detergentes":
        print("Podrías comprar detergente líquido para ropa, jabón en polvo y suavizante.")

# Si el usuario selecciona productos de belleza
elif preferencia == "productos de belleza":
    # Preguntar sobre la categoría de productos de belleza que necesita
    categoria = input("¿Qué tipo de productos de belleza necesitas? (maquillaje, cuidado de la piel, cuidado del cabello): ")
    # Recomendar productos de la categoría seleccionada
    if categoria == "maquillaje":
        print("Podrías comprar una base de maquillaje, un labial y una sombra para ojos.")
    elif categoria == "cuidado de la piel":
        print("Podrías comprar un limpiador facial, una crema hidratante y protector solar.")
    elif categoria == "cuidado del cabello":
        print("Podrías comprar un shampoo, un acondicionador y una mascarilla capilar.")
        
# Si el usuario no selecciona una preferencia válida
else:
    print("Lo siento, no entendí tu preferencia de compra.")