# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 13:35:45 2021

@author: Matheus Grande-Margenfeld
Dette programmet skal kunne løse lineære likningsett på formen for eksempel ax+by+cz=d,
kan ha flere eller færre variabler, og må være like mange likninger som variabler.
    Eks på input: 3 2 1 1 for ligningsettet 3x+2y+z=1 
"""
#Importerer det som er nødvendig fra biblioteket numpy
from numpy import array, linalg
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Funksjon der man får tall hos bruker og legger de i liste, feilsjekker alt, 
#og setter minimum og maksimums lengde for listen og sjekker at alle variablene ikke er 0
def tall(text, minimum, maximum):
   while True:
      try:
         #Bruker skriver inn tallene med mellomrom og flyttall med komma istedenfor punktum. Gjør input-sekvensen om til ei liste, 
         #map gjør at en operasjon blir utført på flere verdier. I dette tilfellet blir alle tallene bruker skriver inn konvertert til float
         z=list(map(float,input(text).replace(",",".").strip().split()))
         #Setter at listen skal være mellom to gitte lengder, og at summen av absoluttverdiene av tallene fremfor variablene er større enn 0, 
         #Dersom summen av tallene er 0 har vi ingen variabel og likningen kan ikke løses fordi det ikke er ei likning. 
         #map blir igjen brukt for å konvertere alle verdiene i den definerte listen minus det siste elementet til absolutte verdier
         assert minimum <= len(z) <= maximum and sum(map(abs, z[:-1]))>0
      except ValueError:
        print("Prøv igjen... sjekk at verdiene du satt inn er tall") #Hvis input ikke er float, prøv på nytt
        continue
      #Hvis lengden på listen ikke er i den gitte lengden 
      #eller at alle variablene er 0 skal koden skrive ut det som står under til konsollet
      except AssertionError:
        print("Skriv inn verdier over lengden: ", minimum,"og under lengden:", maximum, "og at alle variablene ikke er 0")
      else:
          break
   return z
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print("Dette programmet skal løse et likningsett basert på tallene du oppgir, hvis likningen din er for eksempel ax+by+cz=d skriv a b c d i den neste inputen. Husk at du trenger like mange likninger som du har variabler.")
s="j"
#For at koden skal kjøre igjen hvis bruker ønsker det
while s!="":
    #Bruker funksjonen tall til å hente inn tallene i den første likningen, 
    #lengden må være 2 eller lengre siden det skal være en minst en variabel og et tall på andre siden av erlikhetstegnet
    likn=tall("Hva er tallene i den første likninga? ",2, float("inf"))
    #Legger det bakerste tallet i likninga i en egen liste for å kunne bruke linalg.solve senere
    svar=[likn[-1]]
    #Legger de andre tallene i likninga i en egen liste slik at jeg kan bruke linalg.solve senere og omforme den
    likning=[likn[:-1]]
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Benytter funksjonen tall, henter antall nødvendige lister basert på lengden av likningen, 
    #løser så likningene ved bruk av linalgsolve og printer ut løsningen 
    while True:
        try:    
            #Denne skal repetere koden under slik at den henter det nødvendige antall likninger, 
            #bruker lengden av likning - 2 fordi jeg allerede har en av likningene og listen har med tallet på andre siden av erlikhetstegnet
            for i in range (len(likn)-2):
                #Bruker funksjonen over til å hente tallene framfor i den neste likningen og det må være like mange variabler, 
                #derfor må listen bli like lang
                likn1=tall("Tallene i den neste likninga: ", len(likn), len(likn))
                #Legger det bakerste tallet i likninga i listen for å kunne bruke linalg.solve senere
                svar.append(likn1[-1])
                #Legger de andre tallene i likninga i listen slik at jeg kan bruke linalg.solve senere og omforme den
                likning.append(likn1[:-1])
                #Løser likningen ved bruk av linalg.solve, må gjøre listene om til array og omforme den slik at det blir mulig å bruke linalg solve, 
                #bruker derfor lengden til likningen -1 som da er antall variabler og likninger til å omforme den siden det skal være det minste kvadratet
            print(linalg.solve(array(likning).reshape(len(likn)-1,len(likn)-1), array(svar)))
            break
        except:
            print("Prøv igjen... Det er ingen reelle løsninger... Sjekk at likningnene ikke gir to parallelle linjer. Du må skrive inn alle likningene inn på nytt...") #Skriver dette hvis du har gjort en feil
    s=input("Skal du løse et til likningssett? (Trykk enter for nei, og skriv noe som helst og klikk enter for ja): ")