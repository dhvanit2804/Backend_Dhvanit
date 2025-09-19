#include<stdio.h>

int main() {
	int a[5],i,j,temp;
	
	printf("\nEnter Array Elements\n");
	for (i = 0; i<5;i++){
		printf("\nEnter %d Elements: ",i);
		scanf("%d", &a[i]);
	}
	
	printf("\nArray Elements Are\n");
	for (i=0;i<5;i++){
		printf("\nA[%d] : %d",i,a[i]);
	}
	
	for(i=0;i<5;i++){
		for(j=i+1;j<5;j++){
			if(a[i]>a[j]){
				temp = a[i];
				a[i] = a[j];
				a[j] = temp;
			}
		}
	}
	
	printf("\n\nArray Elements in Ascending Order\n");
	for(i=0;i<5;i++){
		printf("\nA[%d] : %d",i,a[i]);
	}
	
	for(i=0;i<5;i++){
		for(j=i+1;j<5;j++){
			if(a[i]<a[j]){
				temp = a[i];
				a[i] = a[j];
				a[j] = temp;
			}
		}
	}
	
	printf("\n\nArray Elements in Descending Order\n");
	for(i=0;i<5;i++){
		printf("\nA[%d] : %d",i,a[i]);
	}
	
	return 0;
	
}
