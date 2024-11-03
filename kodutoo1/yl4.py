def binarySearch(loend, otsitav, low, high):

    # Repeat until the pointers low and high meet each other
    # Otsistav on arv mille indeksid loendist otsime. 
    # Jätan https://www.programiz.com/dsa/binary-search lehelt laenatud koodi alles inglisekeelsed mid, low ja hugh, 
    # sest need kirjeldavad koodi paremini kui eestikeeles
    while low <= high:

        mid = low + (high - low)//2

        if otsitav == loend[mid]:
            return mid

        elif otsitav > loend[mid]:
            low = mid + 1

        else:
            high = mid - 1

    return -1

loend = [3, 4, 5, 6, 7, 8, 9]
otsitav = 6

result = binarySearch(loend, otsitav, 0, len(loend)-1)

if result != -1:
    print("Otsitav element asub indeksil: " + str(result))
else:
    print("Elementi ei leitud")