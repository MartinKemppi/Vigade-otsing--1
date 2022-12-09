from math import* #popravlenie poradka
print("Ruudu karakteristikud")
a=float(input("Sisesta ruudu külje pikkus => ")) #prisvoenie edinic, izmenenia v skobkax
S=a**2
print("Ruudu pindala", S)
P=4*a
print("Ruudu ümbermõõt", P)
di=a*sqrt(2) #math ne nuzen
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud") #skobka ne nuzna
b=float(input("Sisesta ristküliku 1. külje pikkus => ")) #objavlenie peremenoj
c=float(input("Sisesta ristküliku 2. külje pikkus => ")) #objavlenie peremenoj
S=b*c
print("Ristküliku pindala", S) #izmenenie v skobkax, kovicki
P=2*b+c*2 #ubrani skobki i popravlena formula
print("Ristküliku ümbermõõt", P)
di=sqrt(b**2+c**2) #math ne nuzen i voznesenie v kvadrat
print("Ristküliku diagonaal", round(di,2)) #okruglenie do sotix
print()
print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus => ")) #objavlenie peremenoj, izmenenia v skobkax
d=2*r #izmenenie formuli
print("Ringi läbimõõt", d) 
S=float(pi*r**2) #objavlenie peremenoj, izmenenie formuli
print("Ringi pindala", round(S,2)) #okruglenie do sotix
C=2*pi*r #izmenenie v formule
print("Ringjoone pikkus", round(C,2)) #okruglenie do sotix
