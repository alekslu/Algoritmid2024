# Loome massiivi suurusega `size`
size = 10
index_map = [None] * size  # Massiiv, mis toimib meie räsitabelina

# Funktsioon väärtuse lisamiseks massiivi
def insert(key, value):
    """
    Lisab võtme ja väärtuse räsitabelisse.
    Indeks arvutatakse võtme modulo tabeli suurusega.
    """
    index = key % size  # Indeksi arvutamine võtme abil
    index_map[index] = value  # Väärtuse salvestamine vastavale indeksile

# Funktsioon väärtuse otsimiseks massiivist
def get(key):
    """
    Tagastab väärtuse vastavalt antud võtmele.
    Kui väärtust pole, tagastab None.
    """
    index = key % size  # Indeksi arvutamine võtme abil
    return index_map[index]  # Tagastab vastava indeksi väärtuse

# Funktsioon võtme ja väärtuse kustutamiseks massiivist
def delete(key):
    """
    Kustutab väärtuse, seades vastava indeksi väärtuse None-ks.
    """
    index = key % size  # Indeksi arvutamine võtme abil
    index_map[index] = None  # Kustutamine, määrates väärtuse None-ks

# Lisame mõned väärtused
insert(15, "Element 1")  # Key: 15, Value: "Element 1"
insert(25, "Element 2")  # Key: 25, Value: "Element 2"
insert(35, "Element 3")  # Key: 35, Value: "Element 3"

# Otsime väärtusi
print("Väärtus võtmega 15:", get(15))  # Otsib väärtust indeksilt arvutatud võtme abil
print("Väärtus võtmega 25:", get(25))  # Peaks tagastama "Element 2"

# Kustutame ühe võtme ja kontrollime
delete(15)
print("Pärast kustutamist võtmega 15:", get(15))  # Peaks tagastama None

# Massiivi hetkeseis
print("Räsitabeli hetkeseis:", index_map)




'''
2. Analüüsi oma rakenduse aja- ja ruumikomplekssust.

Vastus:
a) Ajaliselt
Lisamine, otsing ja kustutamine: Need toimingud töötavad konstantse ajakompleksusega O(1), kuna kaardistamine toimub otsese indekseerimise kaudu.
Kui aga esineb palju kokkupõrkeid (indeksid kattuvad), võib olla vajalik lisanduvaid samme kokkupõrgete lahendamiseks, mis võib jõudluse halvendada.

b) Ruumiliselt
Ruumikompleksus: O(n), kus n on massiivi suurus.
Massiivi suurus peab olema piisavalt suur, et mahutada kõik võimalikud väärtused ilma liigsete kokkupõrgeteta. 
Kui võtmete väärtused on hõredad (nt väga suured võtmed), võib see raisata mälu. Seda nimetatakse ka ruumimahukaks lähenemiseks.


3. Aruta, kuidas indeksi kaardistamist massiividega saab rakendada reaalses
maailmas.


Vastus:
Index Mapping lähenemist kasutatakse sageli juhtudel, kus on vaja kiiret otsest juurdepääsu fikseeritud suurusega võtmetele või indeksitele:

Näited:
Andmestruktuuride optimeerimine

Kasutatakse lihtsates otsestruktuurides, nagu kaardistamises väärtuste ja indeksite vahel.
Bitmappidega andmete salvestamine

Näiteks kui on vaja salvestada, kas teatud arvud esinevad või mitte (oleku jälgimine), kasutatakse massiivi ja indeksit oleku märkimiseks.
Rakendusnäide: Kontrollida, kas mingi arv on antud andmehulgast leitud (ilma sorteerimiseta või otsinguta).
Graafikute ja maatriksite arvutamine

Suure maatriksi või graafiku esitamine, kus massiiv salvestab iga sõlme (node) otsese naabrustabeli.
Kasutus loendurina (Counter)

Näiteks sageduse loendamisel, kus massiiviga kaardistatakse väärtused otse nende esinemiste arvuks.
Plussid ja miinused:
Plussid: Lihtne, kiire ja efektiivne väikeste andmehulkade jaoks.
Miinused: Mälukasutus võib suureneda, kui kaardistatavad võtmed on hõredalt jaotunud või väga suured.
Suurtes ja keerukates süsteemides (nt andmebaasid) kasutatakse sageli täiustatud räsimist, kuid index mapping jääb oluliseks kontseptsiooniks lihtsamates rakendustes.

'''