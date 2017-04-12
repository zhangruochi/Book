#include "stdio.h"

int strlen(char *a){
	int n;
	for(n=0;*a!='\0'; n++,a++)
		;
	return n;
}

int strlen_two(char *a){
	char *p = a;
	while( *p != '\0')
		p++;
	return p-a;
}

int strcmp(char *a,char *b){
	for(;*a == *b; a++,b++)
		if(*a == '\0')
			return 0;
	return *a - *b;

}

int main(int argc, char const *argv[])
{
	char a[] = "zhangruochi";
	printf("%d\n",strlen(a));
	printf("%d\n",strlen_two(a) );

	return 0;
}