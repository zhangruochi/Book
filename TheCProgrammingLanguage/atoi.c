#include "stdio.h"

int atoi(char x[]);
int atoi_two(char x[]);
void squeeze(char x[],char c);
void strcat(char c[],char d[]);

int main(int argc, char const *argv[])
{
    char c[6] = "12345";
    char a = '1';
    char n[100] = "zhang";
    char m[10] = "ruochi";
    printf("%s\n",c);
    printf("%d\n",atoi(c));
    printf("%d\n",atoi_two(c));
    squeeze(c,a);
    printf("%s\n",c);
    strcat(n,m);
    printf("%s\n",n);
    return 0;
}

int atoi(char x[]){
    int i,sum; 
    i = sum = 0;
    while (x[i] != '\0')
        if(x[i] >= '0' && x[i] <= '9'){
            sum = sum * 10 + x[i] - '0';
            i++;
        }
    return sum;  
}

int atoi_two(char x[]){
    int i,sum;
    sum = 0;
    for(i = 0; x[i] >= '0' && x[i] <= '9'; i++){
        sum = sum * 10 + x[i] - '0';
    }
    return sum;
}

void squeeze(char x[], char c){
    int i,j;
    for (i=j=0;x[i] != '\0'; i++)
        if (x[i] != c)
            x[j++] = x[i];
    x[j] = '\0';    
}

void strcat(char a[],char b[]){
    int i=0, j=0;
    while(a[i] != '\0')
        i++;
    while((a[i++] = b[j++]) != '\0')
        ;

}