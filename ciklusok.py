import math
def ciklusParameterSzamolando(szamEgy:float,szamKetto:float):
    if szamEgy == szamKetto:
        print("Két szám egyenlő!")
        return

    if szamEgy > szamKetto:
        csere: float = szamKetto
        szamEgy = szamKetto
        szamKetto = csere

    szamEgy = math.ceil(szamEgy)
    while szamEgy < szamKetto:
        if(szamEgy == szamKetto-1):
            print(szamEgy)
        else:
            print(szamEgy , end=",")
        szamEgy+=1

