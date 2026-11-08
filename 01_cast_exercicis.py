###
# Exercicis - conversió de tipus (casting)
# Completa els exercicis següents convertint dades entre tipus.
###

# Exercici 1
# Demana a l'usuari quants paquets ha rebut un encaminador. Converteix el valor
# introduït a un nombre enter, suma-hi 1200 paquets i mostra el total.
paquets_rebuts = int(input("Quants paquets ha rebut l'encaminador? "))
total_paquets = paquets_rebuts + 1200
print(f"Total de paquets: {total_paquets}")

# Exercici 2
# Demana a l'usuari la velocitat d'una connexió en Mbps. Converteix el valor
# introduït a un nombre decimal i calcula la velocitat equivalent en MB/s
# dividint-la per 8. Mostra el resultat.
velocitat_mbps = float(input("Velocitat de la connexió en Mbps: "))
velocitat_mbs = velocitat_mbps / 8
print(f"Velocitat equivalent: {velocitat_mbs:.2f} MB/s")
