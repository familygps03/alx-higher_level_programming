#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * main - Generates and prints passwords for the crackme5 executable.
 * @argc: The number of arguments supplied to the program.
 * @argv: An array of pointers to the arguments.
 *
 * Return: Always 0.
 */
int main(int __attribute__((__unused__)) argc, char *argv[])
{
	char password[7], *codex;
	int username_length = strlen(argv[1]), username_sum = 0, max_char = 0;

	codex = "A-CHRDw87lNS0E9B2TibgpnMVys5XzvtOGJcYLU+4mjW6fxqZeF3Qa1rPhdKIouk";

	password[0] = codex[(username_length ^ 59) & 63];

	for (int index = 0; index < username_length; index++)
		username_sum += argv[1][index];
	password[1] = codex[(username_sum ^ 79) & 63];

	int username_product = 1;

	for (int index = 0; index < username_length; index++)
		username_product *= argv[1][index];
	password[2] = codex[(username_product ^ 85) & 63];

	for (int index = 0; index < username_length; index++)
	{
		if (argv[1][index] > max_char)
			max_char = argv[1][index];
	}
	srand(max_char ^ 14);
	password[3] = codex[rand() & 63];

	int squared_sum = 0;

	for (int index = 0; index < username_length; index++)
		squared_sum += (argv[1][index] * argv[1][index]);
	password[4] = codex[(squared_sum ^ 239) & 63];

	for (int index = 0; index < argv[1][0]; index++)
		max_char = rand();
	password[5] = codex[(max_char ^ 229) & 63];

	password[6] = '\0';
	printf("%s", password);
	return (0);

}
