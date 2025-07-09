#include <stdlib.h>
#include <stdio.h>

int main() {
	char x, y, z;

	x = 'a';
	y = 'b';
	z = 'c';

	printf("stampati come caratteri:\n");
	printf("%c\n", x);
	printf("%c\n", y);
	printf("%c\n", z);

	printf("stampati come interi:\n");
	printf("%d\n", x);
	printf("%d\n", y);
	printf("%d\n", z);

	return EXIT_SUCCESS;
}