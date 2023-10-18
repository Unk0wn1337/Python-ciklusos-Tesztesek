import math
import ciklusok
import random
def tesztesetek():
    print("********** TESZTESETEK ***********")
    print("szamEgy = 12 szamKetto = 9")
    ciklusok.ciklusParameterSzamolando(12,9)
    print("Semmi")
    print("szamEgy = -12 szamKetto = 9")
    ciklusok.ciklusParameterSzamolando(-12,9)
    print("szamEgy = 0, szamKetto = 0")
    ciklusok.ciklusParameterSzamolando(0, 0)
    print("")
    print("szamEgy = Pi, szamKetto = 5")
    ciklusok.ciklusParameterSzamolando(math.pi,5)
    print("\nszamEgy = random , szamKetto = random")
    ciklusok.ciklusParameterSzamolando(random.randint(-100,100),random.randint(-300,600))

