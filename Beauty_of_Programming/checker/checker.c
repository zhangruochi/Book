//编程之美中的中国象棋问题，主要难点在只能用1字节来位置变量

#include "stdio.h"

#define HALF_BITS_LENGTH 4
#define FULLMASK 255
#define LMASK  (FULLMASK << HALF_BITS_LENGTH)    //11110000
#define RMASK  (FULLMASK >> HALF_BITS_LENGTH)    //00001111
//这个宏将b的右边设置为n
#define RSET(b,n)  (b = (( b & LMASK) | (n)))
//这个宏将b的左边设置为n 
#define LSET(b,n)  (b = (( b & RMASK) | (n << HALF_BITS_LENGTH)))
//这个宏得到b的右边的值
#define RGET(b) ( RMASK & b)
//这个宏得到b的左边的值
#define LGET(b) ((LMASK & b) >> HALF_BITS_LENGTH)
//定义宽度
#define GRIDW 3

int main(){
    unsigned char b = 0;
    // b 的高位存储 A 的位置， 地位存储 B 的位置
    for(LSET(b,1); LGET(b) <= GRIDW*GRIDW; LSET(b, (LGET(b) + 1))){
        for(RSET(b,1); RGET(b) <= GRIDW*GRIDW; RSET(b, (RGET(b) + 1))){
            if(LGET(b) % GRIDW != RGET(b) % GRIDW)
                printf("A = %d; B= %d \n",LGET(b),RGET(b));
        }
    }

    printf("\n\n\nan more efficent way......\n\n\n");

    struct {
        unsigned char a:4;
        unsigned char b:4;
    } i;

    for(i.a=1; i.a<=9; i.a++){
        for(i.b=1; i.b<=9; i.b++){
            if (i.a % 3 != i.b % 3)
                printf("A = %d; B= %d \n", i.a,i.b);
        }
    }
}
