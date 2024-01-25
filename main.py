import random


teilnehmer = []



def teilnehmerabfrage():
    while True:
        eingabe = input("""Bitte gib einen Namen ein und bestätige mit 'Enter', wenn alle Teilnehmer ihren Namen
eingetragen haben, drücke nur 'Enter' zum Starten
    > """)
        if eingabe == "":
            if len(teilnehmer) < 4:
                teilnehmerabfrage()
            break
        teilnehmer.append(eingabe)

        if len(teilnehmer) == 16:
            break
        if len(teilnehmer) < 4:
            print(f"""
{teilnehmer[-1]} ist Teilnehmer {len(teilnehmer)}/16 
Es fehlen noch mindestens {4-len(teilnehmer)} zum Starten!
            """)

        else:
            print(f"""
{teilnehmer[-1]} ist Teilnehmer {len(teilnehmer)}/16
Jetzt kann gestartet werden! 
""")


teilnehmerabfrage()


print(f"""
Es gibt {len(teilnehmer)} Teilnehmer!
Die Namen der Teilnehmer sind:, {teilnehmer}""")

spiele_berechnung = list(teilnehmer)
spiele = []
anzahl_schleifendurchläufe = len(teilnehmer)
while anzahl_schleifendurchläufe > 0:
    a = 0
    b = 1
    for i in spiele_berechnung:
        if b >= len(spiele_berechnung):
            break
        spiele.append(f"{spiele_berechnung[a]} vs {spiele_berechnung[b]}")
        b += 1

    del spiele_berechnung[0]
    anzahl_schleifendurchläufe -= 1

print(spiele)
global x
x = 0
global teilnehmer_1, teilnehmer_2, teilnehmer_2_vorher, teilnehmer_1_vorher
teilnehmer_1 = 0
teilnehmer_1_vorher = 0
teilnehmer_2 = 0
teilnehmer_2_vorher = 0

def zufall_spiel_erstellen(übrigen_spiele, teilnehmer):
    global teilnehmer_1, teilnehmer_2
    teilnehmer_1 = random.randint(0, len(teilnehmer)-1)
    teilnehmer_2 = random.randint(0, len(teilnehmer)-1)
    if teilnehmer_2 < teilnehmer_1:
        teilnehmer_1_tausch = teilnehmer_1
        teilnehmer_2_tausch = teilnehmer_2
        teilnehmer_2 = teilnehmer_1_tausch
        teilnehmer_1 = teilnehmer_2_tausch
    spiel = f"{teilnehmer[teilnehmer_1]} vs {teilnehmer[teilnehmer_2]}"
    if spiel in übrigen_spiele:
        return spiel
    else:
        spiel = ""
        return spiel

def berechnen_spiele(teilnehmer):
    global teilnehmer_1, teilnehmer_1_vorher, teilnehmer_2, teilnehmer_2_vorher, spiele
    spiel = ""
    übrigen_spiele = list(spiele)
    while spiel not in spiele:
        spiel = zufall_spiel_erstellen(spiele, teilnehmer)
        if spiel != "":
            if übrigen_spiele != [] and spiel in übrigen_spiele:
                übrigen_spiele.remove(spiel)
        if teilnehmer_1 == teilnehmer_1_vorher or teilnehmer_1 == teilnehmer_2_vorher:
            spiel = ""
            if übrigen_spiele == []:
                spiel = zufall_spiel_erstellen(übrigen_spiele, teilnehmer)
        if teilnehmer_2 == teilnehmer_1_vorher or teilnehmer_2 == teilnehmer_2_vorher:
            spiel = ""
            if übrigen_spiele == []:
                spiel = zufall_spiel_erstellen(spiele, teilnehmer)


    teilnehmer_1_vorher = teilnehmer_1
    teilnehmer_2_vorher = teilnehmer_2
    spiele.remove(spiel)
    return spiel



spiele_reihenfolge_schleife = len(spiele)
spiele_reihenfolge = []

while spiele_reihenfolge_schleife > 0:
    spiele_reihenfolge.append(berechnen_spiele(teilnehmer))
    spiele_reihenfolge_schleife -= 1

for element in spiele_reihenfolge:
    print(element + "\n")




