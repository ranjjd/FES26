# EXERCICIS

# Exercici 2: Calculadora senzilla
# Demana a l'usuari dos nombres i una operació (+, -, *, /). Fes l'operació i mostra'n el resultat (gestiona la divisió per zero).
print("\nExercici 2:")
num1 = float(input("Introdueix el primer nombre: "))
num2 = float(input("Introdueix el segon nombre: "))
operacio = input("Introdueix l'operació (+, -, *, /): ").strip()

if operacio == "/" and num2 == 0:
    print("Error: no es pot dividir per zero.")
elif operacio == "+":
    resultat = num1 + num2
    print(f"El resultat és: {resultat}")
elif operacio == "-":
    resultat = num1 - num2
    print(f"El resultat és: {resultat}")
elif operacio == "*":
    resultat = num1 * num2
    print(f"El resultat és: {resultat}")
elif operacio == "/":
    resultat = num1 / num2
    print(f"El resultat és: {resultat}")
else:
    print("Operació no vàlida.")

# Exercici 10: Qualitat d'una connexió de xarxa
# Demana la latència en mil·lisegons i el percentatge de paquets perduts.
# Rebutja una latència negativa o una pèrdua fora del rang del 0 % al 100 %.
# Classifica la connexió com a excel·lent si la latència és de 30 ms o menys i la pèrdua és de l'1 % o menys; bona si és de 80 ms o menys i la pèrdua és
# del 3 % o menys; acceptable si és de 150 ms o menys i la pèrdua és del 5 % o menys; en qualsevol altre cas, deficient.
print("\nExercici 10:")
latencia = float(input("Introdueix la latència en ms: "))
perdua = float(input("Introdueix el percentatge de paquets perduts: "))

if latencia < 0:
    print("La latència no pot ser negativa.")
elif perdua < 0 or perdua > 100:
    print("La pèrdua de paquets ha d'estar entre el 0 % i el 100 %.")
elif latencia <= 30 and perdua <= 1:
    print("La connexió és excel·lent.")
elif latencia <= 80 and perdua <= 3:
    print("La connexió és bona.")
elif latencia <= 150 and perdua <= 5:
    print("La connexió és acceptable.")
else:
    print("La connexió és deficient.")

# Exercici 11: Cost mensual d'un pla de dades
# Demana el tipus de pla (bàsic o plus) i el consum mensual en GB.
# El pla bàsic costa 10 € i inclou 10 GB; cada GB addicional costa 1,50 €.
# El pla plus costa 20 € i inclou 30 GB; cada GB addicional costa 0,75 €.
# Rebutja un consum negatiu o un tipus de pla desconegut. Calcula i mostra el cost total, tenint en compte que no es cobra l'excés si no se supera el límit.
print("\nExercici 11:")
pla = input("Introdueix el tipus de pla (bàsic o plus): ").strip().lower()
consum = float(input("Introdueix el consum mensual en GB: "))

if consum < 0:
    print("El consum no pot ser negatiu.")
elif pla == "bàsic":
    cost = 10
    if consum > 10:
        cost += (consum - 10) * 1.50
    print(f"El cost total és: {cost:.2f} €")
elif pla == "plus":
    cost = 20
    if consum > 30:
        cost += (consum - 30) * 0.75
    print(f"El cost total és: {cost:.2f} €")
else:
    print("Tipus de pla no vàlid.")

# Exercici 12: Accés a un compte de client
# Demana si el compte està actiu, si la contrasenya és correcta i si el codi de doble verificació és correcte. Demana el codi només si el compte és actiu
# i la contrasenya és correcta. Indica si l'accés es denega perquè el compte està desactivat, perquè la contrasenya és incorrecta o perquè falla el codi;
# si totes les comprovacions necessàries són correctes, permet l'accés.
print("\nExercici 12:")
compte_actiu = input("El compte està actiu? (s/n): ").strip().lower()
contrasenya_correcta = input("La contrasenya és correcta? (s/n): ").strip().lower()

if compte_actiu != "s":
    print("Accés denegat: el compte està desactivat.")
elif contrasenya_correcta != "s":
    print("Accés denegat: la contrasenya és incorrecta.")
else:
    codi_correcte = input("El codi de doble verificació és correcte? (s/n): ").strip().lower()
    if codi_correcte == "s":
        print("Accés permès.")
    else:
        print("Accés denegat: el codi de doble verificació és incorrecte.")

# Exercici 13: Diagnòstic d'un router
# Demana si el router està encès, si l'indicador LOS del terminal òptic està encès i si l'indicador d'Internet del router està encès. Indica primer si
# cal encendre el router; si ja està encès, comprova si cal revisar el cable de fibra (LOS encès), si cal contactar amb el proveïdor (Internet apagat) o
# si la connexió funciona correctament. Considera els casos en aquest ordre.
print("\nExercici 13:")
router_encès = input("El router està encès? (s/n): ").strip().lower()

if router_encès != "s":
    print("Cal encendre el router.")
else:
    los_encès = input("L'indicador LOS està encès? (s/n): ").strip().lower()
    internet_encès = input("L'indicador d'Internet està encès? (s/n): ").strip().lower()

    if los_encès == "s":
        print("Cal revisar el cable de fibra.")
    elif internet_encès != "s":
        print("Cal contactar amb el proveïdor.")
    else:
        print("La connexió funciona correctament.")
