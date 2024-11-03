def bubble_sort(arr):
    n = len(arr)
    # Kõigepealt loon välimise tsükli, see on justkui järjehoidja sisemise tsükli jaoks, 
    # et käia läbi kõik elemendid ja need ükshaaval omavahel võrrelda
    for i in range(n):
        print(arr)
        # kasutades listi pikkust ja välise tsükli indeksarvu, käime läbi võrdlused vastavalt kogu listis
        for j in range(0, n - i - 1):
            # kui võrreldav/eelnev indeks on suurem järgmisest, siis vahetame kohad
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# etteantud list mida tuleb
arr = [39, 12, 18, 85, 72, 10, 2, 18]
print("Sorteerimata: ", arr)

bubble_sort(arr)

print("Sorteeritud: ", arr)
