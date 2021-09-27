#include <stdio.h>

#define n 32

int main() {
    int x = 0xff000000;
    printf("%x\n", x | 0xff);

    return 0;
}