---
tags: informatica
date: 2023-07-23
---
[[Compiti delle vacanze 23-24]]
[esercizi](obsidian://open?vault=Francesco%E2%80%99s%20vault%20sync&file=1.areas%2FInformatica%2F25_Esercizi_in_laboratorio.pdf)
#### Esercizio n.2:
```c
#include <stdio.h>

int main() {
    int cont = 0;
    float n, s = 100;
    
    while (s >= 0) {
        printf("Inserisci un numero: ");
        scanf("%f", &n);
        cont++;
        s -= n;
    }
    
    printf("%d\n", cont);
    return 0;
}
```

#### Esercizio n.4:
```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int m1, m2, m3, cont = 0;
    srand(time(NULL));
    
    do {
        m1 = rand() % 2;
        m2 = rand() % 2;
        m3 = rand() % 2;
        cont++;
    } while (m1 != m2 || m2 != m3);
    
    printf("%d\n", cont);
    return 0;
}
```

#### Esercizio n.5:
```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int dado, cont = 0, s = 0;
    srand(time(NULL));
    
    while (s <= 100) {
        dado = rand() % 6 + 1;
        cont++;
        s += dado;
    }
    
    printf("%d\n", cont);
    return 0;
}
```

#### Esercizio n.6:
```c
#include <stdio.h>

int main() {
    int cont = 0, numero;
    
    do {
        printf("Inserisci un numero divisibile per 13: ");
        scanf("%d", &numero);
        if (numero % 13 == 0)
            cont++;
    } while (numero % 13 == 0);
    
    printf("%d\n", cont);
    return 0;
}
```

Ora hai le soluzioni corrette per gli esercizi. Buon lavoro!