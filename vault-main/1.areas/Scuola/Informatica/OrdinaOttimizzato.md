---
tags:
  - informatica
date: 2024-09-30
---
```c
void ordinaO(int v[], int d){
	int mini, j;
	for(int i=0;i<d-1;i++)
		mini=i;
		for(j=i+1;j<d;j++){
			if(v[j]<v[mini])
				mini=j;
		}
	if(i!=mini)
	scambia(&v[i], &v[mini])
}
```