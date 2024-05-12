from moduli.Impostazioni import *
import moduli.FunzioniMenu as FunzioniMenu

def chiediIntero(prompt, da = -INTERO_IMPOSSIBILE, a = INTERO_IMPOSSIBILE):
   """Chiede un intero in ingresso, stampando una frase di richiesta
   il numero deve essere strettamente compreso fra "da" e "a", scartando eventuali input errati"""
   
   uscita = False
   while not uscita:
      s = "s"
      uscitainterna = False
      while not uscitainterna:
         s = input(prompt + ": ")
         if (FunzioniMenu.intero(s)):
            uscitainterna = True
         else:
            print("La stringa inserita non è un numero intero", "\n\n")

      n = int(s)

      if ((n > da) and (n < a)):
         uscita = True
      else:
         print("Il numero inserito non è strettamente compreso fra: ",  da, " e: ", a, "\n\n")

   return n


   

def chiediStringa(prompt):
   """Chiede una stringa in ingresso, stampando una frase di richiesta"""

   uscita = False
   while not uscita:
        s = ""
        s = input(prompt + ": ").strip()
        if (s != ""):
            uscita = True
        else:
            print("La stringa inserita non è valida", "\n\n")
   return s
