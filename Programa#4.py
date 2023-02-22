#Programa cuatro, este programa lo diseñe usando un modulo que aprendí de internet el datatime. Este programa te sugiere que debes de comer 
#dependiendo de que hora del dia sea.
import datetime

now = datetime.datetime.now()
hour = now.hour

if hour >= 6 and hour <= 9:
    print("Debes comer un desayuno saludable que incluya proteínas, carbohidratos complejos y frutas.")
elif hour >= 12 and hour <= 14:
    print("Debes comer un almuerzo equilibrado que incluya proteínas, carbohidratos complejos, verduras y frutas.")
elif hour >= 18 and hour <= 20:
    print("Debes comer una cena ligera que incluya proteínas magras, verduras y carbohidratos complejos.")
else:
    print("En este momento no es recomendable comer, trata de mantener una dieta balanceada y no comer alimentos procesados en exceso.")
