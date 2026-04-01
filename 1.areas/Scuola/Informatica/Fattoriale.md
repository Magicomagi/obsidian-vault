---
tags:
  - informatica
  - funzioni
date: 2023-12-01
---
```c
#include<stdio.h>
int fattoriale(int x){
	int f=1,i;
	for(i=2;i<=x; i++)
		f*=i;
	return f;
}
```