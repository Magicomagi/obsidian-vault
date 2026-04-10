---
tags: informatica
date: 2026-04-10
---
Riassunto — Fondamenti di Calcolo Numerico (Informatica)

1. Definizioni fondamentali
Calcolo numerico: disciplina che implementa algoritmi per risolvere problemi matematici non risolubili analiticamente (integrali, equazioni, valori di funzioni).
Requisiti di un algoritmo:
	•	Passi elementari non ambigui
	•	Numero finito di passi
	•	Efficienza nell’uso delle risorse
Problema numerico: relazione funzionale y = f(x) tra input e output. Ogni problema può avere più algoritmi associati, con precisione diversa.

2. Rappresentazione dei numeri nel calcolatore
Numeri interi
	•	n bit → intervallo [-(2^(n-1)), +(2^(n-1)-1)]
	•	1 bit usato per il segno → solo n-1 bit per il modulo
	•	Overflow: il risultato eccede l’intervallo rappresentabile → la cifra più significativa viene persa
	•	Aritmetica intera: esatta, ma divisione tra interi perde il resto; risultato può andare fuori range



|Tipo        |Byte|Accuratezza  |Intervallo          |
|------------|----|-------------|--------------------|
|signed int  |2   |—            |`[-2^15, 2^15-1]`   |
|unsigned int|2   |—            |`[0, 2^16-1]`       |
|float       |4   |6 cifre dec. |`±{10^-38, 10^38}`  |
|double      |8   |15 cifre dec.|`±{10^-308, 10^308}`|

Numeri reali — Virgola mobile (floating point)
Forma: x = m * B^e
	•	m = mantissa, B = base (10 o 2), e = esponente intero
	•	Struttura in memoria: 1 bit segno + t bit mantissa + q bit esponente
	•	Rappresentazione normalizzata: B^(-1) ≤ |m| < 1
	•	x = 0 → coppia (0, 0) per convenzione
	•	Distribuzione non uniforme: valori molto densi vicino allo 0, molto radi vicino al massimo
	•	Overflow: e > Ms — Underflow: e < Mi

3. Errori numerici
Tipi principali



|Errore            |Causa                                                             |
|------------------|------------------------------------------------------------------|
|**Arrotondamento**|Numero finito di cifre per rappresentare i dati                   |
|**Troncamento**   |Approssimazione di sequenze infinite con un numero finito di passi|

Definizioni e formule
Errore assoluto (1.1):

e = valore_vero − approssimazione


Errore relativo:

ε = e / valore_vero


Errore relativo percentuale:

εp = (e / valore_vero) * 100%


Errore relativo approssimato — usato quando il valore vero non è noto (1.2):

εa = (valore_vero − approssimazione) / approssimazione


Errore relativo iterativo — usato nei metodi iterativi (1.3):

εa = (approssimazione_attuale − approssimazione_precedente) / approssimazione_attuale


Il calcolo si ferma quando |εa| < Σs (tolleranza prefissata).

4. Metodo Babilonese — Radice quadrata
Ricorrenza: s0 = n/2, poi s_k = (s_(k-1) + n/s_(k-1)) / 2
Convergenza: quadratica (le cifre corrette raddoppiano ad ogni iterazione).
Motivo per cui funziona: se sx < √n, allora n/sx > √n → la media aritmetica converge verso √n. Per la disuguaglianza aritmo-geometrica, dalla seconda iterazione in poi tutte le stime sono per eccesso (se n > 1).
Versione iterativa con numero di passi fisso

double radiceBabilonese(double n, int pedice) {
    if (n == 0) return 0;
    double s = n / 2;
    int i;
    for (i = 1; i <= pedice; i++) {
        s = 0.5 * (s + n / s);
        printf("\ns%d = %.12lf", i, s);
    }
    return s;
}


Versione ricorsiva

double radiceBabiloneseRicorsiva(double n, int pedice) {
    if (n == 0) return 0;
    if (pedice == 0) return n / 2;
    double r = radiceBabiloneseRicorsiva(n, pedice - 1);
    return 0.5 * (r + n / r);
}


Nota: la variabile intermedia r serve a evitare che la funzione ricorsiva venga chiamata due volte con gli stessi argomenti nel return.
Versione con errore relativo (numero di passi non noto a priori → do-while)

double radiceBabiloneseErroreRelativo(double n, double errore, int* pedice) {
    if (n == 0) return 0;
    double s = n / 2, precedente;
    *pedice = 0;
    do {
        precedente = s;
        s = 0.5 * (precedente + n / precedente);
        (*pedice)++;
        printf("\ns%d=%lf errore=%lf", *pedice, s, fabs((s - precedente) / s));
    } while (fabs((s - precedente) / s) > errore);
    return s;
}


Versione con errore assoluto

double radiceBabiloneseErroreAssoluto(double n, double errore, int* pedice) {
    if (n == 0) return 0;
    double s = n / 2;
    *pedice = 0;
    do {
        s = 0.5 * (s + n / s);
        (*pedice)++;
        printf("\ns%d=%lf errore=%.12lf", *pedice, s, fabs(sqrt(n) - s));
    } while (fabs(sqrt(n) - s) > errore);
    return s;
}


Nota: l’errore assoluto usa sqrt(n) dalla libreria come riferimento “vero”.

5. Radice cubica — Successione alternativa
Ricorrenza: a0 = 1, a_(n+1) = ((a_n + b/a_n²) / 2)²
Limite: lim → ∞ = ∛b
Converge più lentamente rispetto al metodo babilonese (lineare, non quadratica).

6. Calcolo di e — Serie di Eulero
Formula:

e = Σ(k=0→∞) 1/k! = 1 + 1/1! + 1/2! + 1/3! + ...


Struttura del programma: 4 funzioni — iterativa, ricorsiva, con errore assoluto (usa M_E come riferimento), con errore relativo.

7. Calcolo di π — Serie di Leibniz
Derivazione: da Gregory (1671), arctan(x) = x - x³/3 + x⁵/5 - ..., applicata in x=1:

π/4 = Σ(n=0→∞) (-1)^n / (2n+1) = 1 - 1/3 + 1/5 - 1/7 + ...


Criterio di Leibniz — convergenza garantita se:
	1.	an > 0 per ogni n (segni alterni)
	2.	an → 0
	3.	La serie è monotona decrescente (an ≥ a_(n+1))
Versione iterativa

double leibnizIt(int num) {
    int i;
    double s = 0;
    for (i = 0; i <= num; i++)
        s += pow(-1, i) / (2 * i + 1);
    return s;
}
// Nel main: printf("%.16lf", 4 * leibnizIt(n));


Versione ricorsiva

double leibnizRic(int num) {
    if (num == 0) return 1;
    return pow(-1, num) / (2 * num + 1) + leibnizRic(num - 1);
}


Con errore assoluto (usa M_PI come riferimento)

double leibnizEA(double imp, int* mn) {
    *mn = -1;
    double s = 0;
    do {
        (*mn)++;
        s += (pow(-1, (*mn))) / (2 * (*mn) + 1);
    } while (fabs(4 * s - M_PI) > imp);
    return s;
}


Con errore relativo

double leibnizER(double imp, int* mn) {
    *mn = -1;
    double s = 0, prec;
    do {
        (*mn)++;
        prec = s;
        s += (pow(-1, (*mn))) / (2 * (*mn) + 1);
    } while (fabs((s - prec) / s) > imp);
    return s;
}


8. Radice quadrata — Metodo di Newton
Ricorrenza: calcola 1/√a (inverso della radice)

x0 = 1/a
x_k = (x_(k-1) / 2) * (3 - a * x_(k-1)²)


Il risultato finale si ottiene come 1 / x_k.

9. Seno — Serie di Taylor
Formula:

sin(x) = Σ(n=0→∞) (-1)^n * x^(2n+1) / (2n+1)!


Struttura: 4 funzioni — sinTaylorIt, sinTaylorRic, sinTaylorEA (errore assoluto), sinTaylorER (errore relativo).

10. Integrazione numerica — Calcolo approssimato delle aree
Ipotesi: funzione limitata, definita e continua su [a, b].
Motivazione: quando la primitiva F(x) non è calcolabile analiticamente (es. e^(-x²)), l’integrazione numerica è l’unico approccio praticabile.
Metodo dei rettangoli
Divide [a,b] in n intervalli di ampiezza h = (b-a)/n. Per ogni intervallo usa il valore della funzione nel punto centrale.

A = h * Σ f(xc)    dove xc = a + h/2 + i*h


double rettangoli(double a, double b, int inter) {
    double h = (b - a) / inter, area = 0;
    double m = a + h / 2;
    int i;
    for (i = 1; i <= inter; i++) {
        area += h * f(m);
        m += h;
    }
    return area;
}


Metodo dei trapezi
Usa le aree di n trapezi: basi f(xi) e f(xi+1), altezza h.

Sn = h/2 * [f(a) + 2*Σ f(xi) + f(b)]


double trapezi(double a, double b, int inter) {
    double h = (b - a) / inter, area = 0;
    int i;
    for (i = 1; i <= inter; i++) {
        area += (f(a) + f(a + h)) * h / 2;
        a += h;
    }
    return area;
}


Metodo di Cavalieri-Simpson
Approssima la funzione con parabole su doppi intervalli di ampiezza 2h. n deve essere pari.

A = h/3 * [f(xi) + 4*f(xi+h) + f(xi+2h)]


double CavalieriSimpson(double a, double b, int inter) {
    double h = (b - a) / inter, area = 0;
    int j;
    for (j = 1; j <= inter / 2; j++) {
        area += h / 3 * (f(a) + 4 * f(a + h) + f(a + 2 * h));
        a += 2 * h;
    }
    return area;
}


Metodo Montecarlo
Genera punti casuali nel rettangolo che contiene la curva e conta quanti cadono sotto la funzione.

double montecarlo(double sin, double des, int pti) {
    int i, dentro = 0;
    double x, y;
    srand(time(NULL));
    for (i = 1; i <= pti; i++) {
        x = rand() / (double)RAND_MAX * (des - sin) + sin;
        y = rand() / (double)RAND_MAX * f(des);
        if (y <= f(x)) dentro++;
    }
    return (des - sin) * f(des) * dentro / (float)pti;
}


Confronto tra metodi



|Metodo           |Rapidità|Precisione|Note                                         |
|-----------------|--------|----------|---------------------------------------------|
|Rettangoli       |Elevata |Scarsa    |Usa punto centrale                           |
|Trapezi          |Media   |Media     |Usa estremi                                  |
|Cavalieri-Simpson|Bassa   |Elevata   |`n` deve essere pari                         |
|Montecarlo       |—       |Variabile |Probabilistico, utile per geometrie complesse|

Pattern ricorrenti nel codice C da ricordare
do-while vs for: quando il numero di iterazioni non è noto a priori (errore come criterio di stop) → sempre do-while. Quando il numero è fissato → for.
Passaggio per indirizzo (int* pedice): usato per restituire valori aggiuntivi (es. il numero di iterazioni effettuate) senza usare variabili globali.
fabs(): valore assoluto per double (da <math.h>). Non usare abs() che opera su interi.
pow(-1, n): calcola (-1)^n per gestire serie a segni alterni.
Tolleranza: si calcola come pow(10, -esponente) dove l’esponente è inserito dall’utente.​​​​​​​​​​​​​​​​