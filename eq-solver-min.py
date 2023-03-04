# -*- coding: utf-8 -*-
from numpy import array, linalg
def tall(text, minimum, maximum):
   while True:
      try:
         z=list(map(float,input(text).replace(",",".").strip().split())); assert minimum <= len(z) <= maximum and sum(map(abs, z[:-1]))>0
      except ValueError:
        print("Prøv igjen... sjekk at verdiene du satt inn er tall") #Hvis input ikke er float, prøv på nytt
        continue
      except AssertionError:
        print("Skriv inn antall verdier mellom:", minimum,"og mindre antall enn:", maximum,"og at alle variablene ikke er 0")
      else:
          break
   return z
print("Dette programmet skal løse et likningsett basert på tallene du oppgir, hvis likningen din er for eksempel ax+by+cz=d skriv a b c d i den neste inputen. Husk at du trenger like mange likninger som du har variabler.")
s="j"
while s!="":
    while True:
        try:
            likn=tall("Hva er tallene i den første likninga? ",2, float("inf"))
            svar,likning=[likn[-1]],[likn[:-1]]
            for i in range (len(likn)-2):
                likn1=tall("Tallene i den neste likninga: ", len(likn), len(likn))
                svar.append(likn1[-1]); likning.append(likn1[:-1])
            print(linalg.solve(array(likning).reshape(len(likn)-1,len(likn)-1), array(svar)))
            break
        except:
            likning,svar=[],[]; print("Prøv igjen... Det er ingen reelle løsninger... Sjekk at likningnene ikke gir to parallelle linjer. Du må skrive inn alle likningene inn på nytt...") #Skriver dette hvis du har gjort en feil
    s=input("Skal du løse et til likningssett? (Trykk enter for nei, og skriv noe som helst og klikk enter for ja): ")