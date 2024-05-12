from moduli.Impostazioni import *
import moduli.ChiediDati as ChiediDati


MINMENU = 0
"""
calcola l'indice dell'ultima voce di menù
"""
MAXMENU = len(MENU) - 1
uscita = False
while not uscita:
   if (MENU[MAXMENU] == INATTIVA):
      MAXMENU -= 1
   else:
      uscita = True
   
MESSAGGIOERR = "Scelta non prevista"

SEPARATORE_MENU = "-" * (len(PREMESSAGGIO) + len(MIDMESSAGGIO))



def creaVocimenu(tup):
   """
   Funzione che genera le voci di menù originate dalla tupla di stringhe in ingresso
   la sequenza contiene tutte le voci diverse da "<Inattiva>"

   """

   voci = ""
   for i in range(len(tup)):
      if (tup[i] != INATTIVA):
         voci = voci + PREMESSAGGIO + str(i) + MIDMESSAGGIO + tup[i] + "\n"

   return voci


def menu(tup):
   """
   funzione che stampa un menù con le voci generate da CreaVociMenu()
   """

   uscita = False
   while not uscita:
      print (3 * "\n" + SEPARATORE_MENU)
      scelta = ChiediDati.chiediIntero(creaVocimenu(tup), MINMENU - 1, MAXMENU + 1)
      if (tup[scelta] != INATTIVA):
         uscita = True
      else:
         print (MESSAGGIOERR, "\n")

   return scelta



def intero(stringa):
   """
   restituisce True se il parametro in ingresso ?n numero intero
   """

   if (stringa.isnumeric()):
      return True
   else:
      return False