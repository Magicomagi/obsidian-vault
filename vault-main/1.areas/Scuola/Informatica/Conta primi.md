---
tag: informatica, funzioni
date: 2023-11-30
---
````c
include<stdio.h>
int primo(int x){
	if(x<2)
		return 0;
	for(int i=2; i<=x/2; i++)
		if(x%i==0)
			return 0;
	return 1;
}


int contaPrimi(int min, int max){
	int i, cont=0;
	for(i=min; i<=max; i++)
		if(primo(i))
			cont++;
	return cont;
}


int inputInt(int min){
	int x;
	do{
		pritf("inserisci un numero:");
		scanf("%d", &x);
		if(x<min)
			pritf("\a errore, il numero deve essere >= %d", x);
	}while(x<min);
	return x;
}


main(){
int a=inputInt(0), b=inputInt(0);
printf("tra %d e %d ci sono %d numeri primi", a, b, )
}
```