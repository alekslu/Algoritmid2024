def insertion_sort(loend):
    # Alustame teisest elemendist
    for i in range(1, len(loend)):
        print(loend)
        vaadeldav = loend[i]
        j = i - 1 

        # Liigutame suuremaid elemente ühe koha võrra paremale, et tekiks tühi koht kuhu vaadeldav paigutada
        while j >= 0 and loend[j] > vaadeldav:
            loend[j + 1] = loend[j]
            j -= 1
        
        # Paigutame vadeldava/võrreldava oma kohale
        loend[j + 1] = vaadeldav

# Testime antud loendiga
loend = [12, 11, 13, 5, 6, 7]
print("Algne loend:", loend)
insertion_sort(loend)
print("Sorteeritud loend:", loend)

'''
Insertion Sort on tõhus, sest ta ei liigu pidevalt kogu listi läbi vaid mingi osa piires.
Kui loend on juba osaliselt sorteeritud ja elemendid oma õigtele kohtadel, siis pole vaja liigutusteks teha
üleliia palju samme ning seetõttu on see ka tõhus. Täielikult sorteerimata listi puhul võib olla insertion ajamahukas, sest 
kogu list tuleb läbi käia
'''