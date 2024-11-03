#n =	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	...
#xn =	0	1	1	2	3	5	8	13	21	34	55	89	144	233	377	...

def fibonacci(n):
    # Baasjuhtumid 0 ja 1 ning tingimus, et negatiivne ei saa olla sisendarv
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n < 0:
        return "Ei saa olla negatiivne"
    else:
        return fibonacci(n - 1) + fibonacci(n - 2) # Rekursiivne samm

#Kasutan loodud funktsiooni, kirjutan tulemuse konsooli
print("Fibonacci number on:", fibonacci(9))
