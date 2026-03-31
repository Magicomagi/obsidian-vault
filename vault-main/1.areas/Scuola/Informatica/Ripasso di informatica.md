---
tag: informatica
date: 2024-09-16
---
1. 
```c
int min(int x, int y){
	if(x<y)
		return x;
	return y;
}
```
--- 
2. 
```c
int positivo(int x){
	if(x>=0)
		return 1;
	return 0;
}
```

```c
int positivo(int x){
return x>=0;
}

```
---
3. 
```c
void scambia(float*x, float*y){
float temp;
temp=*x;
*x=*y;
*y=temp;
}
```
---
4. 
```c
int sommaDivisori(int min, int max){
srand(time(NULL));
int n=rand ()%(max-min+1)min, somma=0;
for(int i=1; i<n(1/2); i++)
	if(n%i==0)
		somma+=i;
return somma
}
```
