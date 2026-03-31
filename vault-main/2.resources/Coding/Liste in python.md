---
tag: informatica
date: 2024-01-28
---

```python

basketball_bag["scarpe", "casacca"]

basketball_bag.append("calze di ricabio") 	#append aggiunge calze di ricambio alla lista basketball_bag (solo un oggetto)
basketball_bag.extend(["maglia termica", "borraccia"])	 #extend, aggiunge maglia termica e borraccia alla lista basketball_bag
basketball_bag = basketball_bag + ["mentality"] 	#è uguale ai 2 precedenti
basketball_bag.insert(0, "asciugamano") 	#aggiunge ascigamano all'inizio della lista

basketball_bag.clear() 	#svuota la lista
basketball_bag.remove("mentality") 		#rimuove mentality dalla lista
basketball_bag.pop(1)


print(basketball_bag)

```
iniziano da 0, non da 1

si possono usare i numeri negativi per partire dalla fine della lista


