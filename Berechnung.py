def berechnen_spiele(teilnehmer, x):
    spiel = ""
    while spiel not in spiele:
        spiel = f"{teilnehmer[x]} vs {teilnehmer[x + 1]}"
        x += 2
        print(spiel)
    spiele.remove(spiel)
    return spiel



spiele_reihenfolge_schleife = len(spiele)
spiele_reihenfolge = []

while spiele_reihenfolge_schleife > 0:
    spiele_reihenfolge.append(berechnen_spiele(teilnehmer, x))
    spiele_reihenfolge_schleife -= 1
    print(spiele_reihenfolge)


