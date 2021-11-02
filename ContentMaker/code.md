## main
```c
 #include <stdio.h>

int main() {
 printf("Hello, World!");
 // ex1
 //printf(``hello world"");
 //ex2
 //printf("test \\c \c"); // unkown escape sequence

}
 ```
## variables
```c
 #include<stdio.h>

int main()
{
    printf("************************* Fahr to Celsius *************************\n");
    float fahr, celsius;
    float lower, upper, step;
    lower = 0;
    upper =200;
    step = 20;
    while(lower <= upper) {
        celsius = 5.0 * (lower - 32.0) / 9.0;
        printf("%3.0f\t%6.1f\n", lower, celsius);
        lower = lower + step;
    }

    printf("************************* Celsius to Fahr *************************\n");

    lower =0;
    upper = 200;
    step= 20;
    while(lower <= upper) {
        fahr = 9.0 * (lower + 32) / 5.0;
        printf("%3.0f\t%6.1f\n", lower, fahr);
        lower = lower + step;
    }

}
 ```
