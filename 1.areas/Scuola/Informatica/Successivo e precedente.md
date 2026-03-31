---
tag: informatica, funzioni
date: 2023-11-30
---
````c
int inputInt(){
	int x;
	pritf("inserisci un numero:");
	scanf("%d", &x);
	return x;
}


int successivo(int n1){
	return n1+1;
}


int precedente(int n1){
	return n1-1;
}


mdoain{
printf("il successivo di %d e' %d", n, sucessivo(n));
printf("il precedente di %d e' %d", n, precedente(n));
}
```