---
tags:
  - informatica
  - funzioni
date: 2023-12-01
---
````c
int isTriangolo(float a1, float b1, float c1){
	if(a1+b1<c1)
		return 0;
	if(c1+b1<a1)
		return 0;
	if(c1+c1<b1)
		return 0;
	return 1
}
```
