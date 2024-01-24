
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

