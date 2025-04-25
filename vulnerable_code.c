#include <stdio.h>
#include <string.h>

int main() {
    char str1[10];
    char str2[10] = "ThisIsTooLong";
    strcpy(str1, str2); // Buffer Overflow

    char query[100];
    sprintf(query, "SELECT * FROM users WHERE name = \"%s\"", userInput); // SQL Injection

    char *password = "12345"; // Hardcoded password

    return 0;
}
