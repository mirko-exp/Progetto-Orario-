from moduli.ChiediDati import *
from moduli.FunzioniMenu import *
from moduli.Impostazioni import *
import moduli.FunzioniOrario



def menu():
    scelta = FunzioniMenu.Menu(MENU)
    return scelta

def main():
    scelta_utente = menu()
    
    uscita = False
    
    while not uscita:
        if (scelta_utente == 0):
            uscita = True
        else:
            if (scelta_utente == 1): 
                orario_istituto = ChiediDati.ChiediStringa("Inserisci il percorso del file dell'orario dei docenti")
                classe_istituto = ChiediDati.ChiediStringa("Inserisci una delle classi dell'orario")
                FunzioniOrario.docenti_classe(orario_istituto, classe_istituto)
            
            elif (scelta_utente == 2):
                orario_istituto = ChiediDati.ChiediStringa("Inserisci il percorso del file dell'orario dei docenti")
                docente_istituto = ChiediDati.ChiediStringa("Inserisci un docente dell'orario")
                FunzioniOrario.orario_docente(orario_istituto, docente_istituto)
            
            elif (scelta_utente == 3):
                orario_istituto = ChiediDati.ChiediStringa("Inserisci il percorso del file dell'orario dei docenti")
                docente_istituto = ChiediDati.ChiediStringa("Inserisci un docente dell'orario")
                FunzioniOrario.ore_diposizione(orario_istituto, docente_istituto)
                
            elif (scelta_utente == 4):
                orario_istituto = ChiediDati.ChiediStringa("Inserisci il percorso del file dell'orario dei docenti")
                ora = ChiediDati.ChiediStringa("Inserisci un giorno dell'orario")
                giorno = ChiediDati.ChiediStringa("Inserisci un' ora dell'orario")
                FunzioniOrario.ore_disponibile(orario_istituto, ora, giorno)
           
            scelta_utente = menu()
    
    
main()           