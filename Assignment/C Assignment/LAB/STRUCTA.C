#include<stdio.h>
#include<conio.h>

struct Student
{
	char name[50];
	int rno;
	float marks;
};

void main()
{
	struct Student s[3];
	int i;

	clrscr();

	printf("\Enter details of 3 students:\n");
	for(i=0;i<3;i++)
	{
		printf("\nStudent %d\n",i+1);

		printf("\nEnter name: ");
		gets(s[i].name);
		fflush(stdin);

		printf("\nEnter roll number: ");
		scanf(" %d", &s[i].rno);
		fflush(stdin);

		printf("\nEnter marks: ");
		scanf(" %f", &s[i].marks);
		fflush(stdin);
	}

	printf("\n---Student Details ---\n");
	for(i=0;i<3;i++)
	{
		printf("\nStudent %d",i+1);
		printf("\Name : %s",s[i].name);
		printf("\nRoll Number: %d",s[i].rno);
		printf("\nMarks: %.2f",s[i].marks);
	}
	getch();
}