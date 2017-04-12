#include "stdio.h"
int main(int argc, char const *argv[])
{	
	for(int i = 0;i<=99;i++)
		printf("%6c%c", '*',( i%10 == 9 || i ==100-1) ? '\n' : ' ');
	return 0;
}