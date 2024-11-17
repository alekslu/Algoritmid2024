def binary_search(arr, target):

    low, high = 0, len(arr) - 1 # defineeritakse algus ja lõpp ning selle abil hakatakse massiivi poolitama
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target: # targetit otsitakse poolitatud massiivi keskelt
            return mid
        elif arr[mid] < target: # järgmise kahe tingimusega liigutatakse massiivi järjest kokkupoole
            low = mid + 1
        else:
            high = mid - 1
    return "Ei leidnud otsitavat" 

# Näidisandmed (sorteeritud massiiv)
arr = [10, 15, 23, 45, 70, 85, 100]
target = 70

# Tulemus
tulemus = binary_search(arr, target)
print("Otsitav asub indeksil: ", tulemus)

"""
2. Võrrelge teoreetilises analüüsis valminud Binary Search'i ja Linear Search'i
aegkomplekssust.

Vastus:
*Linear Search: Kontrollib iga elementi järjest. Halvimal juhul peab see läbima kogu massiivi.
*Binary Search: Jagab massiivi igal sammul pooleks ning on seetõttu oluliselt kiirem suurte sorteeritud andmekogude korral. 
Näiteks, kui massiivis on 1024 elementi, vajab Binary Search maksimaalselt umbes  log2(1024) = 10 sammu

*Linear 1024 sammu vs Binary Search 10 sammu - tohutu vahe.

3. Tooge näide stsenaariumist, kus Binary Search on kasulikum kui Linear
Search, selgitage.

Vastus:
*Kiirus: Kuna Binary Search jagab massiivi pooleks igal sammul, leiab see väärtuse O(logn) ajaga. 
Suurtes massiivides (nt n=1000000) tähendab see ligikaudu 20 sammu, 
võrreldes Linear Searchi O(n)-ga, mis võib halvimal juhul läbida 1000000 sammu.
*Optimeeritud ressursikasutus: Vähem kontrolle tähendab väiksemat arvutusvõimsuse vajadust ja väiksemat viivitust.

"""