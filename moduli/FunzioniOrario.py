#from Impostazioni import *
import os
import sys
sys.path.append('C:\Mattia lavori\Compiti mattia\INI\SPHINX\moduli')

def docenti_classe(file_orario, classe):
    
    """
    Scrive in un file l'elenco dei docenti di una data classe

    Primo parametro   - accetta in ingresso il percorso del file da analizzare
    Secondo parametro - accetta in ingresso una classe dell'orario"""
    
    if not os.path.exists(file_orario):
        print("-" * 24)
        print("\nErrore: file inesistente\n")
        print("-" * 24)
        
    else:
        elenco_docenti = []
        orario = open(file_orario, "r")
        file_output_aperto = open(FILE_OUTPUT, "w")
        
        riga = orario.readline().strip()
        while (riga != ""):
            riga = riga.split(SEPARATORE) 
            if (classe.upper().strip() in riga):
                elenco_docenti.append(riga[0].strip())
            riga = orario.readline().strip() #Lettura della riga successiva
        
        if (len(elenco_docenti) == 0):
            file_output_aperto.write("La classe inserita non è presente nell'orario")
        else:
            #scrittura nel file dei docenti
            for docente in elenco_docenti:
                file_output_aperto.write(docente + "\n")
            
        orario.close()
        file_output_aperto.close()
        
def conta_ore(riga_file):
    
    """
    Conta il numero di ore 

    Primo parametro - accetta in ingresso una riga del file già separata, depurata e inserita in una lista
    """
    
    conta_ore = 0
    for ora in riga_file:
        ora = ora.strip()
        if ((ora != "") and (ora != riga_file[0]) and (ora != RICEVIMENTO)): #riga_file[0] = docente
            conta_ore += 1
                
    return conta_ore - 1
    
def orario_docente(file_orario, docente):
    
    """
    Scrive in un file l'orario di un determinato docente e numero totale delle ore del docente

    Primo parametro   - accetta in ingresso il percorso del file da analizzare
    Secondo parametro - accetta in ingresso un docente dell'orario
    """
    
    if not os.path.exists(file_orario):
        print("-" * 24)
        print("\nErrore: file inesistente\n")
        print("-" * 24)
        
    else:
        orario = open(file_orario, "r")
        file_output_aperto = open(FILE_OUTPUT, "w")
        orario.readline() #Lettura della prima riga di intestazione
        orario.readline() #Lettura della seconda riga di intestazione
        riga = orario.readline().strip() #Lettura del primo docente
        
        while (riga != ""):
            riga = riga.split(SEPARATORE) #Creazione di una lista contente ogni ora della settimana
            if (riga[0].strip() == docente.upper()):
                ore_docente = conta_ore(riga)
                
                #Scrittura nel file dell'orario
                file_output_aperto.write("Orario di: " + docente.upper() + "\n" + "\n")
                for giorno in SETTIMANA:
                    file_output_aperto.write(giorno)
                file_output_aperto.write("\n")
                for i in range(len(ORE)):
                    file_output_aperto.write(ORE[i] + " " + riga[i+1] + "  " + riga[i+9] + "  " + riga[i+17] + "  " + riga[i+25] + "  " + riga[i+33] + "\n")
                file_output_aperto.write(100 * "-" + "\n")
                file_output_aperto.write("Le ore totale di lezione (SENZA RICEVIMENTI) di " + docente.upper() + " sono: " + str(ore_docente))
               
            riga = orario.readline().strip() #Lettura della riga successiva
            
        orario.close()
        file_output_aperto.close()
        
def ore_diposizione(file_orario, docente):
    """
    Scrive in un file le ore a disposizione di un determinato docente

    Primo parametro   - accetta in ingresso il percorso del file da analizzare
    Secondo parametro - accetta in ingresso un docente dell'orario
    """
    
    if not os.path.exists(file_orario):
        print("-" * 24)
        print("\nErrore: file inesistente\n")
        print("-" * 24)
        
    else:
        conta_disposizione = 0
        orario = open(file_orario, "r")
        file_output_aperto = open(FILE_OUTPUT, "w")
        riga = orario.readline().strip()
        while (riga != ""):
            riga = riga.split(SEPARATORE)
            if (docente.upper().strip() == riga[0].strip()):
                for ora in riga:
                    if (DISPOSIZIONE == ora.strip()):
                        conta_disposizione += 1
            riga = orario.readline().strip() #Lettura della riga successiva
            
        file_output_aperto.write("Il docente " + docente.upper() + " ha " + str(conta_disposizione) + " ore di disposizione")
        
        file_output_aperto.close()
        orario.close()

def ore_disponibile(file_orario, ora, giorno):
    """
    Scrive in un file l'elenco dei docenti che hanno lezione a una determinata ora
    di un determinato giorno della settimana 

    Primo parametro   - accetta in ingresso il percorso del file da analizzare
    Secondo parametro - accetta in ingresso un'ora
    Terzo parametro   - accetta in ingresso un giorno
    """
    
    if not os.path.exists(file_orario):
        print("-" * 24)
        print("\nErrore: file inesistente\n")
        print("-" * 24)
        
    else:
        elenco_docenti = []
        
        orario = open(file_orario, "r")
        file_output_aperto = open(FILE_OUTPUT, "w")
        orario.readline() #Lettura della prima riga di intestazione
        orario.readline() #Lettura della seconda riga di intestazione
        
        riga = orario.readline().strip() #Lettura del primo docente
        while (riga != ""):
            riga = riga.split(SEPARATORE)
            posizione = GIORNI_SET[giorno] + int(ora)
            if (riga[posizione] != "   "):
                elenco_docenti.append(riga[0].strip())
            riga = orario.readline().strip() #Lettura della riga successiva
            
        if (len(elenco_docenti) == 0):
            file_output_aperto.write("Nessun docente ha lezione alla " + str(ora) + "ª ora del " + giorno)
        else:
            #scrittura nel file dei docenti
            for i in range(len(elenco_docenti)):
                file_output_aperto.write(elenco_docenti[i] + "\n")
        
        file_output_aperto.close()
        orario.close()