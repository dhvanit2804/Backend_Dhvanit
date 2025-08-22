#include<stdio.h>
#include<conio.h>

void main()
{
	FILE *file;
	char filename[] = "data.txt";
	char text[] = "Hello, this is test string!";
	char ch;

	clrscr();

	file = fopen(filename, "w");
	if(file == NULL){
		printf("\nError opening file for writting.");
		getch();
		return;
	}
	fprintf(file, "%s",text);
	fclose(file);
	printf("\nString written to file successfully.");

	// 2. Open the file
	file = fopen(filename, "r");
	if(file==NULL){
		printf("\nError opening file for reading.");
		getch();
		return;
	}
	printf("\nContents of the file:");
	while((ch = fgetc(file)) != EOF){
		printf("%c",ch);
	}
	fclose(file);
	getch();
}