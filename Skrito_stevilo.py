# -*- coding: utf-8 -*-

print "Casino figa v zepu"
print "Začetek igre: Ugani 'srečno' število!"
print "Ugibaj svoje srečno število toliko časa, da ga najdeš."


iskano_stevilo = raw_input("Vaša srečna številka je: ")

srecna_stevilka = "13"


while iskano_stevilo != srecna_stevilka:
    if iskano_stevilo > srecna_stevilka:
        print("Vaša srečna številka je manjša.")
        iskano_stevilo=raw_input("Vaša srečna številka je:")
    elif iskano_stevilo < srecna_stevilka:
        print("Vaša srečna številka je večja.")
        iskano_stevilo=raw_input("Vaša srečna številka je:")

print "No pa si našel/a srečno 13tico. Za nagrado dobiš poln žakelj sreče."
