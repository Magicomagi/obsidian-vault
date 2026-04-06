---
tag:
date: 2025-04-22
---
## Modalità:
- Normal mode: Modalità di default, per navigare e modificare.
- Insert mode: Modalità di inserimento testo (i, a).
- Visual mode: Modalità di selezione (v).
- Command mode: Per eseguire comandi (:).

## Comandi di Base   
|            |                      |
| ---------- | -------------------- |
| Comando    | Descrizione          |
| vim <file> | Apri un file in Vim. |
| :w         | Salva il file.       |
| :q         | Esci.                |
| :wq        | Salva ed esci.       |
| :q!        | Esci senza salvare.  |
| :e <file>  | Apri un nuovo file.  |
| :w <file>  | Salva con nome.      |
  
## Navigazione

|            |                                         |
| ---------- | --------------------------------------- |
| Comando    | Descrizione                             |
| h, j, k, l | Muoviti (sinistra, giù, su, destra).    |
| gg         | Vai all’inizio del file.                |
| G          | Vai alla fine del file.                 |
| :n         | Vai alla linea n.                       |
| w          | Vai all’inizio della parola successiva. |
| b          | Vai all’inizio della parola precedente. |
| %          | Salta alla parentesi corrispondente.    |
| Ctrl + u   | Scorri metà schermo verso l’alto.       |
| Ctrl + d   | Scorri metà schermo verso il basso.     |

## Inserimento Testo

|         |                                  |
| ------- | -------------------------------- |
| Comando | Descrizione                      |
| i       | Inserisci prima del cursore.     |
| I       | Inserisci all’inizio della riga. |
| a       | Inserisci dopo il cursore.       |
| A       | Inserisci alla fine della riga.  |
| o       | Inserisci una nuova riga sotto.  |
| O       | Inserisci una nuova riga sopra.  |
| Esc     | Torna alla modalità normale.     |

## Modifica Testo

|   |   |
|---|---|
|Comando|Descrizione|
|x|Cancella il carattere sotto il cursore.|
|dw|Cancella una parola.|
|dd|Cancella una riga.|
|d$|Cancella fino alla fine della riga.|
|u|Annulla l’ultima modifica.|
|Ctrl + r|Ripeti l’ultima modifica annullata.|
|yy|Copia una riga.|
|p|Incolla dopo il cursore.|
|r<char>|Sostituisci il carattere sotto il cursore con <char>|
|ciw|Cambia l’intera parola.|

## Selezione e Modifica Avanzata

|   |   |
|---|---|
|Comando|Descrizione|
|v|Entra in Visual mode per selezionare caratteri.|
|V|Seleziona una riga intera.|
|Ctrl + v|Entra in Visual Block mode per selezionare un blocco.|
|y|Copia la selezione.|
|d|Taglia la selezione.|
|>|Indenta la selezione.|
|<|Riduci l’indentazione della selezione.|
## Ricerca e Sostituzione 

|                      |                                                            |
| -------------------- | ---------------------------------------------------------- |
| Comando              | Descrizione                                                |
| /testo               | Cerca “testo” nel file.                                    |
| ?testo               | Cerca “testo” all’indietro.                                |
| n                    | Vai all’occorrenza successiva della ricerca.               |
| N                    | Vai all’occorrenza precedente della ricerca.               |
| :s/vecchio/nuovo/g   | Sostituisci “vecchio” con “nuovo” nella riga attuale.      |
| :%s/vecchio/nuovo/g  | Sostituisci “vecchio” con “nuovo” nell’intero file.        |
| :%s/vecchio/nuovo/gc | Sostituisci in tutto il file, confermando ogni occorrenza. |

  

  

  

  

  

Lavorare con Più File

  

|   |   |
|---|---|
|Comando|Descrizione|
|:e <file>|Apri un nuovo file in una nuova finestra.|
|:split <file>|Dividi la finestra e apri un nuovo file.|
|:vsplit <file>|Dividi la finestra verticalmente.|
|Ctrl + w + h/j/k/l|Passa alla finestra sinistra/giù/su/destra.|
|:bn|Vai al buffer successivo.|
|:bp|Vai al buffer precedente.|

  

  

  

  

  

Comandi Utili Vari

  

|   |   |
|---|---|
|Comando|Descrizione|
|.|Ripeti l’ultimo comando eseguito.|
|:noh|Rimuove l’evidenziazione della ricerca.|
|:set number|Mostra i numeri di riga.|
|:set nonumber|Nasconde i numeri di riga.|
|:set paste|Attiva modalità “paste” per evitare formattazioni strane|
|:set nopaste|Disattiva modalità “paste”.|
|:syntax on|Attiva la colorazione della sintassi.|

  

  

  

  

  

Uscire da Vim

  

|   |   |
|---|---|
|Comando|Descrizione|
|:wq|Salva ed esci.|
|:q!|Esci senza salvare.|
|:wqa|Salva tutti i file aperti ed esci.|

  

  

  

  

Con questa guida hai tutto ciò che ti serve per iniziare con Vim!