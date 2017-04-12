#include "stdio.h"

int strindex(char source[], char pattern[]);
int main(int argc, char const *argv[])
{
	char source[] = "zhangruochi";
	char pattern[] = "ruochi";
	printf("%d\n",strindex(source,pattern));	
	return 0;
}

int strindex(char source[],char pattern[]){
	int i,j,k;
	for (i=0;source[i] != '\0'; i++){
		for (j=i,k=0;source[j] == pattern[k] && pattern[k] != '\0'; j++,k++)
			;
		if (k > 0 && pattern[k] == '\0')
			return i;
	}
	return -1;

}