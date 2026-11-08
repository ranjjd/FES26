###
# exercicis-basics.py
# Exercicis per practicar els conceptes apresos a les lliçons.
###

print("\nExercici 1: Imprimir missatges")
print("Escriu un programa que imprimeixi el teu nom i la teva ciutat en línies separades.")

### Completa aquí

print("El meu nom és Rania.")
print("La meva ciutat és Mataró.")

print("--------------")

print("\nExercici 2: Mostra els tipus de dades de les variables següents:")
print("Utilitza la comanda 'type()' per determinar el tipus de dades de cada variable.")
a = 15
b = 3.14159
c = "Hola món"
d = True
e = None

### Completa aquí

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print("--------------")

print("\nExercici 3: Conversió de tipus")
print("Converteix la cadena \"12345\" a un enter i després a un float.")
print("Converteix el float 3.99 a un enter. Què passa?")

### Completa aquí

print(int("12345"))
print(float("12345"))
print(int(3.99)) #els decimals que hi havia es perden.

print("--------------")

print("\nExercici 4: Variables")
print("Crea variables per al teu nom, edat i alçada.")
print("Utilitza f-strings per imprimir una presentació.")

# "Hola! Em dic Marc, tinc 40 anys i faig 1.75 metres"
#name = "Marc"
#age = 40

### Completa aquí

nom="Rania"
edat=18
alcada=1.73
print(f"Hola! Em dic {nom}, tinc {edat} anys i faig {alcada} metres.")


print("--------------")

print("\nExercici 5: Nombres")
print("1. Crea una variable amb el nombre PI (sense assignar una variable)")
print("2. Arrodoneix el nombre amb round()")
print("3. Fes la divisió entera entre el nombre resultant i el nombre 2")
print("4. El resultat hauria de ser 1")


PI = 3.1416
nombre_resultant = round(PI)
divisio = nombre_resultant/2 
print(f"El resultat de la divisió és: {divisio}")

print("--------------")

print("\nExercici 6: Conversor de temperatura")
print("Demana a l'usuari una temperatura en graus Celsius.")
print("Converteix aquest valor a Fahrenheit amb la fórmula: F = (C * 9/5) + 32")
print("Mostra els dos valors amb un missatge clar.")

### Completa aquí

temperatura = input("Introdueix una temperatura en graus Celsius: ")
temperatura= float(temperatura)
temp_farenheit = (temperatura * 9/5) + 32
print(f"La temperatura en Fahrenheit és: {temp_farenheit}")


print("--------------")

print("\nExercici 7: Calculadora de propina")
print("Demana el total d'un compte i el percentatge de propina.")
print("Calcula quant és la propina i el total final que s'ha de pagar.")
print("Mostra els resultats amb 2 decimals.")

### Completa aquí

total_compte, percentatge_propina= input("Introdueix el total del comte i el percentatge de propina : ").split()
total_compte= float(total_compte)
percentatge_propina= float(percentatge_propina)
propina = total_compte * (percentatge_propina / 100)
total_final = total_compte + propina
print(f"El total del compte és {total_compte:.2f}€ i el de la propina és {propina:.2f}€.")
print(f"El total final que s'ha de pagar és {total_final:.2f}€.")

print("--------------")

print("\nExercici 8: Validador de contrasenya simple")
print("Demana una contrasenya a l'usuari.")
print("Comprova si té almenys 8 caràcters.")
print("Mostra 'Contrasenya vàlida' o 'Contrasenya no vàlida'.")

### Completa aquí

contrasenya = input("Introdueix una contrasenya: ")
