###
# EXERCICIS (while)
###

# Exercici 1: Compte enrere
# Imprimeix els números del 10 a l'1 fent servir un bucle while.
print("\nExercici 1:")
numero = 10
while numero >= 1:
  print(numero)
  numero -= 1

# Exercici 3: Factorial d'un número
# Demana a l'usuari que introdueixi un número enter positiu. Calcula el seu factorial fent servir un bucle while.
# El factorial d'un número enter positiu és el producte de tots els números de l'1 fins a aquest número. Per exemple, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nExercici 3:")
factorial = 1
numero = int(input("Introdueix un número enter positiu: "))
while numero > 1:
  factorial *= numero
  numero -= 1
print(f"El factorial és: {factorial}")

# Exercici 7: Suma fins al zero
# Demana a l'usuari que introdueixi números enters. Ves sumant els números introduïts fins que l'usuari introdueixi el 0.
# Al final, imprimeix la suma total. El 0 només serveix per acabar i no s'ha de sumar.
print("\nExercici 7:")

suma = 0
numero = int(input("Introdueix un número enter (0 per acabar): "))

while numero != 0:
  suma += numero
  numero = int(input("Introdueix un altre número enter (0 per acabar): "))

print(f"La suma total és: {suma}")

# Exercici 9: Seqüència de Fibonacci
# Demana a l'usuari quants termes de la seqüència de Fibonacci vol veure. Imprimeix aquest nombre de termes fent servir un bucle while.
# La seqüència comença per 0 i 1; cada terme següent és la suma dels dos anteriors.
print("\nExercici 9:")

termes = int(input("Quants termes de Fibonacci vols veure? "))
anterior = 0
actual = 1
comptador = 0

while comptador < termes:
  print(anterior)
  seguent = anterior + actual
  anterior = actual
  actual = seguent
  comptador += 1

# Exercici 10: Joc d'endevinar el número
# El número secret és el 7. Demana a l'usuari que provi d'endevinar-lo i continua demanant números amb un bucle while fins que l'encerti.
# Després de cada intent incorrecte, indica si el número secret és més gran o més petit.
print("\nExercici 10:")

numero_secret = 7
intent = int(input("Endevina el número secret: "))

while intent != numero_secret:
  if intent < numero_secret:
    print("El número secret és més gran.")
  else:
    print("El número secret és més petit.")
  intent = int(input("Torna-ho a provar: "))

print("Correcte! Has endevinat el número.")

print(f"La suma dels números parells fins a 20 és: {suma_parells}")
