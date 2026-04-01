---
tags:
  - note
  - dataview
date: 2024-07-18
---
### Concetti di Base


#### Tipi di Query

- **Tabelle**: Visualizzano i dati in formato tabellare.
- **Liste**: Visualizzano i dati come elenchi.
- **Calendari**: Visualizzano i dati in un calendario mensile.
- **Task**: Visualizzano tutte le task nel vault
### Esempi di Utilizzo

#### Creare una Tabella

Per creare una tabella con tutti gli appunti con il tag `#progetto`:

```markdown
```dataview
table titolo, autore
from #progetto
```


#### Creare una Lista

Per creare una lista di tutti gli appunti modificati nell'ultima settimana:

```markdown
```dataview
list
from ""
where file.mtime >= date(today) - dur(7 days)
```


#### Creare un Calendario

Per creare un calendario degli appunti con il tag `#evento`:

```markdown
```dataview
calendar from #evento
```


### Proprietà dei File

Dataview può accedere a diverse proprietà dei file, come il nome, la data di creazione e modifica, e le front matter YAML. Esempio di front matter YAML:

```yaml
---
titolo: "Esempio di Nota"
autore: "Mario Rossi"
data: 2023-01-01
---
```

#### Utilizzare le Proprietà nei Filtri

Per filtrare gli appunti creati da "Mario Rossi":

```markdown
```dataview
table titolo, data
from ""
where autore = "Mario Rossi"
```


### Funzioni Utili

- `date(today)`: Restituisce la data odierna.
- `dur(7 days)`: Restituisce un periodo di 7 giorni.
- `contains(field, value)`: Verifica se un campo contiene un valore specifico.

### Esempi Avanzati

#### Sommare Valori Numerici

Per sommare i valori di un campo `ore` in appunti con il tag `#lavoro`:

```markdown
```dataview
table sum(ore) as "Totale Ore"
from #lavoro
```


#### Visualizzare Scadenze Future

Per visualizzare una lista di scadenze future ordinate per data:

```markdown
```dataview
list titolo, data_scadenza
from ""
where data_scadenza >= date(today)
sort data_scadenza asc
```
