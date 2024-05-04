import sys
sys.path.append('C:\Mattia lavori\Compiti mattia\INI\SPHINX\moduli')
from Impostazioni import *





def ChiediIntero(prompt, da = -INTERO_IMPOSSIBILE, a = INTERO_IMPOSSIBILE):
   """funzione con il compito di chiedere un intero in ingresso, stampando una frase di richiesta
   il numero deve essere strettamente compreso fra "da" e "a", scartando eventuali input errati"""
   uscita = False
   while not uscita:
      s = "s"
      uscitainterna = False
      while not uscitainterna:
         s = input(prompt + ": ")
         if (Funzioni.Intero(s)):
            uscitainterna = True
         else:
            print("La stringa inserita non è un numero intero", "\n\n")

      n = int(s)

      if ((n > da) and (n < a)):
         uscita = True
      else:
         print("Il numero inserito non è strettamente compreso fra: ",  da, " e: ", a, "\n\n")

   return n


   

def ChiediStringa(prompt):
   """funzione con il compito di chiedere una stringa in ingresso, stampando una frase di richiesta"""

   uscita = False
   while not uscita:
        s = ""
        s = input(prompt + ": ").strip()
        if (s != ""):
            uscita = True
        else:
            print("La stringa inserita non è valida", "\n\n")
   return s
