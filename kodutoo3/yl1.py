def linear_search(arr, target): # sisenditeks on nimekiri ja otsitav element
    for index in range(len(arr)): # käiakse läbi kõik indeksid nimekirja terves ulatuses
        if arr[index] == target: # kui väärtus indeksi kohal on võrdne otsitava väärtusega, siis tagastatakse selle koha indeks
            return index
    return -1

# Näidisandmed
arr = [10, 23, 45, 70, 11, 15]
target = 70

# Tulemus
tulemus = linear_search(arr, target)
print("Otsitav asub indeksil: ", tulemus)


"""
2. Analüüsige oma algoritmi aja- ja ruumikomplekssust.

Vastus:
Ajakompleksus:
* Halvimal juhul kontrollitakse kõiki elemente.
Seega on ajaline keerukus O(n), kus n on massiivi pikkus.
* Parimal juhul leitakse element esimesel positsioonil O(1).

Ruumikompleksus:
* Mälu maht ei sõltu nimekirja suurusest ja meetd ise kasutab vähe muutujaid, seetõttu vajab ta konstantselt ainult lisamäl O(1).
Praktikas tähendaks see seda, et isegi kui andmemaht on väga suur, siis alogrimti enda mäluvajadus ei suurene. 
Alogritm on lihtsalt sellisel juhul väga aeglane

3. Arutlege lühidalt, kuidas Linear Search algoritmi saab kasutada reaalmaailma
rakendustes ja millised on selle piirangud.

Vastus:

*Positiivne:
Väikesed andmekogumid. Linear Search sobib hästi väikeste nimekirjade puhul, kus keerulisemate otsingualgoritmide kasutamine oleks liiast.
Järjestamata andmed. Kuna Linear Search ei nõua andmete eelnevat sorteerimist, saab seda kasutada nimekirjades, mis ei ole mingil viisil struktureeritud.

*Negatiivne:
Aeglaseks muutumine suurte andmekogumite korral. Suur andmekogum võib Linear Searchi puhul tähendada märkimisväärset viivitust, eriti kui otsitavat elementi pole.

"""