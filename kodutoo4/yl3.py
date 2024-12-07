
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None  # Viit järgmisele sõlmele

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size  # Loome tühja tabeli suurusega `size`
    
    def hash_function(self, key): # Räsifunktsioon, mis arvutab võtme modulo tabeli suurusega.
        return key % self.size
    
    def insert(self, key, value):
        index = self.hash_function(key)
        # Kui indeks on tühi, loome uue sõlme
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            # Liigume lingitud nimekirja lõppu ja lisame uue sõlme
            current = self.table[index]
            while current:
                if current.key == key:
                    # Kui võti on juba olemas, uuendame väärtust
                    current.value = value
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = Node(key, value)  # Lisame uue sõlme lõppu

    def get(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None  # Võtit ei leitud
    
    def delete(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None
        while current:
            if current.key == key:
                if prev is None:
                    # Eemaldame esimese sõlme
                    self.table[index] = current.next
                else:
                    # Eemaldame sõlme, ühendades eelneva ja järgmise
                    prev.next = current.next
                return
            prev = current
            current = current.next

# Testime räsitabelit
size = 10
hash_table = HashTable(size)

# Lisame väärtused
hash_table.insert(15, "Element 1")
hash_table.insert(25, "Element 2")  # Samasse indeksisse kui 15
hash_table.insert(35, "Element 3")  # Samasse indeksisse kui 15 ja 25

# Otsime väärtusi
print("Väärtus võtmega 15:", hash_table.get(15))
print("Väärtus võtmega 25:", hash_table.get(25))
print("Väärtus võtmega 35:", hash_table.get(35))

# Kustutame ühe võtme
hash_table.delete(25)
print("Pärast kustutamist võtmega 25:", hash_table.get(25))



'''
2. Võrdle separate chaningu efektiivsust open addressing meetodiga ajalise ja
ruumilise komplekssuse mõttes.

Vastus:
*Ajakompleksus
Separate chaining: Keskmiselt O(1), halvim O(n) (kokkupõrke korral).
Open adressing: Keskmiselt O(1), halvim O(n) (kõrge täitumusega).

*Ruumikompleksus
Separate chaining: O(n+m), kus n on massiivi suurus ja m on kokkupõrked.
Open adressing: O(n) kuna kasutatakse ainult massiivi.

3. Aruta separate chaning kasutamise plusse ja miinuseid räsitabelites.

Vastus:
*Positiivne:
1. Töötab hästi ka suure täitumuse korral;
2. Elementide eemaldamine lingitud nimekirjast on lihtne, ei pea massiivi ümber hakkama tõstma;
3. Toimib hästi ka dünaamiliselt muutuva andmekogumiga;

*Negatiivne:
1. Lingitud nimekirjad vajavad lisamälu;
2. Kokkupõrgete korral on otsingud aeglasemad;
3. Ehituslikult keerulisem;
'''