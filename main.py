import ciklusok
import Tesztesetek
# Felhaszánló csak olyan szamKetto-t tudjon megadni ami nagymint a szamEgy
szamEgy:int = int(input("Kérek egy számot"))
szamKetto:int = int(input("Kérek egy számot"))
while (szamEgy >= szamKetto):
    print("b-nek nagyobbnak kell lennie szamEgynel")
    szamKetto:int = int(input(f"Adj {szamEgy}-nel nagyobbat"))

ciklusok.ciklusParameterSzamolando(szamEgy,szamKetto)


#Tesztesetek.tesztesetek()
