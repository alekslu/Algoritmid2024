class Stack:
    def __init__(self):
        self.stack = [None] * 100  # Eelseadistatud suurusega list
        self.top = -1  # Algne positsioon, mis näitab tühja virna
    
    def push(self, item): # Lisab elemendi virna tippu
        if self.top < len(self.stack) - 1:
            self.top += 1
            self.stack[self.top] = item
        else:
            print("Virn on täis")

    def isEmpty(self): # Kontrollib kas virn on tühi
        return self.top == -1
    
    def pop(self): #Eemaldab ja tagastab virna tipu elemendi.
        if not self.isEmpty():
            item = self.stack[self.top]
            self.stack[self.top] = None  # Puhastab väärtuse
            self.top -= 1
            return item
        else:
            return "Virn on tühi"
        
    def length(self): # Tagastab virna pikkuse
        return self.top + 1  # Kuna top on viimane täidetud indeks, indeksid algavad 0ist

#Kasutame loodud funktsioone
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

stackPikkus = stack.length()

print("Virna sisu:", stack.stack[:stack.top + 1])  # Näitab elemente tipuni

while stackPikkus > 0:
    stackPikkus = stack.length()  
    print("Eemaldatud element:", stack.pop())
print("Virna sisu peale eemaldamist:", stack.stack[:stack.top + 1])

#Sellise struktuuri keerukus on alati O(n), sest iga kord kui elemente lisatakse või eemaldatakse, 
# tuleb teha seda ühe elemendi kaupa
