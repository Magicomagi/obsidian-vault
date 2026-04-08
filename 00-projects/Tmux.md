---
date: 2026-04-09
tags:
  - informatica
  - note
---
# Guida Rapida a tmux

> **tmux** è un terminal multiplexer: permette di gestire più sessioni, finestre e pannelli in un'unica finestra del terminale. I processi rimangono attivi anche se chiudi la finestra o ti disconnetti.

`tmux`Avvia una nuova sessione
`tmux ls`Elenca tutte le sessioni attive
`tmux attach -t nome`Riconnettiti a una sessione specifica

### 1. Gestione Pannelli (Splits)

- `Ctrl + b` poi `%` : Dividi in verticale.
- `Ctrl + b` poi `"` : Dividi in orizzontale.
- `Ctrl + b` poi `o` : Passa al pannello successivo.
- `Ctrl + b` poi `x` : Chiudi il pannello corrente.
- `Ctrl + b` poi `z` : Ingrandisci/Rimpicciolisci il pannello (Zoom).

### 2. Gestione Finestre (Tabs)

- `Ctrl + b` poi `c` : Crea una nuova finestra.
    
- `Ctrl + b` poi `n` : Vai alla finestra successiva.
    
- `Ctrl + b` poi `p` : Vai alla finestra precedente.
    
- `Ctrl + b` poi `0...9` : Vai a una finestra specifica per numero.
    

### 3. Sessioni e Distacco

- `Ctrl + b` poi `d` : **Detach** (esci dalla sessione lasciandola attiva).
    
- `Ctrl + b` poi `s` : Mostra l'elenco delle sessioni per passare da una all'altra.