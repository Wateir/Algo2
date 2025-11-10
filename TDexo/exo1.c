#include <stdio.h>

int main(int argc, char **argv){
	int a, b, c = ((int)argv[1]), ((int)argv[2]), ((int)argv[3]);
	if (a > b && a > c){
		printf("%d",a);
	}
	if (b > a && b > c){
		printf("%d",b);
	}
	else{
		printf("%d",c);
	}
	printf("\n");
	return 0;
}
