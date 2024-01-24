
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

spiele_berechnung = teilnehmer
spiele = []
anzahl_schleifendurchläufe = len(teilnehmer)
while anzahl_schleifendurchläufe > 0:
    a = 0
    b = 1
    for i in spiele_berechnung:
        if b >= len(teilnehmer):
            break
        spiele.append(f"{teilnehmer[a]} vs {teilnehmer[b]}")
        b += 1

    del spiele_berechnung[0]
    anzahl_schleifendurchläufe -= 1

print(spiele)


spiele_reihenfolge_schleife = len(spiele)
spiele_reihenfolge = []
spiel = 0

def ausrechnen_spiel():
    len(teilnehmer) * 2 - 4

while spiele_reihenfolge_schleife > 0:
    spiele_reihenfolge.append(spiele[spiel])
    spiele += len(teilnehmer) * 2 -
    if spiele >


