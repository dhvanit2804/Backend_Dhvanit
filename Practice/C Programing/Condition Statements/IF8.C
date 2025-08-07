#include<stdio.h>
#include<conio.h>

void main()
{
	int age;
	char id[50];
	clrscr();
	printf("\Enter Age : ");
	scanf("%d",&age);
	printf("\nDo You have ID Proof(Y/N): ");
	gets(id);

	if(age>=18 && (id =="Y" || id == "y"))
		printf("Eligible to vote");
	else
		printf("Not eligible to vote");
	getch();
}