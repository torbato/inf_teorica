// #include <stdio.h>

// int main() {
// 	int a;
// 	int b;
// 	int *c;
// 	int *d;

// 	a = 9;
// 	c = &a;

// 	b = a;		// assegnamento fra variabili 9
// 	d = c;		// assegnamento fra puntatori &a

// 	a = 12;
// 	printf("a = %d\n", a); // 12
// 	printf("b = %d\n", b); // 9
// 	printf("*c = %d\n", *c); // 12
// 	printf("*d = %d\n", *d); // 12
// }

#include <stdio.h>

int main() {
	// int a;
	// a = 2;
	// printf("%d\n", a);

	int *c;
	*c = 2;
	printf("%d\n", *c);
}