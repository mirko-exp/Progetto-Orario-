import moduli.ChiediDati as ChiediDati
import moduli.FunzioniMenu as FunzioniMenu
from moduli.Impostazioni import *
import moduli.FunzioniOrario as FunzioniOrario



def menu():
    scelta = FunzioniMenu.menu(MENU)
    return scelta

def main():
    scelta_utente = menu()
    
    uscita = False
    
    while not uscita:
        if (scelta_utente == 0):
            uscita = True
        else:
            if (scelta_utente == 1): 
                orario_istituto = ChiediDati.chiediStringa("Inserisci il percorso del file dell'orario dei docenti")
                classe_istituto = ChiediDati.chiediStringa("Inserisci una delle classi dell'orario")
                file_output = ChiediDati.chiediStringa("Inserisci il percorso del file in cui scrivere l'elaborazione della funzione scelta")
                FunzioniOrario.docenti_classe(orario_istituto, classe_istituto, file_output)
            
            elif (scelta_utente == 2):
                orario_istituto = ChiediDati.chiediStringa("Inserisci il percorso del file dell'orario dei docenti")
                docente_istituto = ChiediDati.chiediStringa("Inserisci un docente dell'orario")
                file_output = ChiediDati.chiediStringa("Inserisci il percorso del file in cui scrivere l'elaborazione della funzione scelta")
                FunzioniOrario.orario_docente(orario_istituto, docente_istituto, file_output)
            
            elif (scelta_utente == 3):
                orario_istituto = ChiediDati.chiediStringa("Inserisci il percorso del file dell'orario dei docenti")
                docente_istituto = ChiediDati.chiediStringa("Inserisci un docente dell'orario")
                file_output = ChiediDati.chiediStringa("Inserisci il percorso del file in cui scrivere l'elaborazione della funzione scelta")
                FunzioniOrario.ore_diposizione(orario_istituto, docente_istituto, file_output)
                
            elif (scelta_utente == 4):
                orario_istituto = ChiediDati.chiediStringa("Inserisci il percorso del file dell'orario dei docenti")
                ora = ChiediDati.chiediStringa("Inserisci un'ora dell'orario")
                giorno = ChiediDati.chiediStringa("Inserisci un giorno dell'orario")
                file_output = ChiediDati.chiediStringa("Inserisci il percorso del file in cui scrivere l'elaborazione della funzione scelta")
                FunzioniOrario.ore_disponibile(orario_istituto, ora, giorno, file_output)
           
            scelta_utente = menu()
    
    
main()           