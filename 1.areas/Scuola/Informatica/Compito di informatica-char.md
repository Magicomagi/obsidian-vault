---
tag: informatica
date: 2023-11-10
---
```c
#include <stdio.h>
int main() {
    char car;
    int somMa = 0, somMi = 0, sommaNon = 0;
    for (int i = 0; i < 10; ++i) {
      printf("Inserisci 1 carattere: ");
      scanf(" %c", &car);
        if ((car >= 'A' && car <= 'Z') || (car >= 'a' && car <= 'z')) {
            if (car >= 'A' && car <= 'Z') {
                somMa += (int)car;
            } else {
                somMi += (int)car;
            }
        } else {
            sommaNon += (int)car;
        }
    }
    printf("Somma maiuscoli: %d\n", somMa);
    printf("Somma minuscoli: %d\n", somMi);
    printf("Somma non alfabetici: %d\n", sommaNon);

}
```

```c
#include <stdio.h>

int main() {
    char car;
    int cont = 0, n = 0;
    do {
	    printf("Inserisci carattere: ");
        scanf(" %c", &car);
        n++;

        if (car >= 'A' && car <= 'Z') {
            cont++;
        }
    } while (cont < 10);
    printf("Hai inserito %d caratteri, inclusi %d maiuscoli.\n", n, cont);
}
```

```c
#include <stdio.h>

int main() {
    char car;
    do {
        printf("Inserisci un carattere alfabetico maiuscolo: ");
        scanf(" %c", &car);
    } while (car < 'A' || car > 'Z');
    printf("Hai inserito: %c\n", car);
}
```

```c
#include <stdio.h>

int main() {
    char scelta;
    do {
        printf("Inserisci 'S' per Sì o 'N' per No: ");
        scanf(" %c", &scelta);
    } while (scelta != 'S' && scelta != 'N');
    printf("Hai scelto: %c\n", scelta);
}
```