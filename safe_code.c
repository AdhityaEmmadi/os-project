#include <stdio.h>
#include <string.h>

int main() {
    char str1[10];
    strncpy(str1, "Safe", sizeof(str1) - 1); // Safe copy

    char query[100];
    snprintf(query, sizeof(query), "SELECT * FROM users WHERE name = ?", userInput); // Parameterized, safe

    char *pwd = getPasswordFromUser(); // Not hardcoded

    return 0;
}
