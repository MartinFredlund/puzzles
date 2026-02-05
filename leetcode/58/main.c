#include <stdio.h>
#include <string.h>
int lengthOfLastWord(char* s) {

    s[strcspn(s, "\n")] = 0;

    int length = 0;
    int i = strlen(s)-1;

    while (i >= 0 && (s[i] == ' ' || s[i] == '"')) {
        i--;
    }

    while (i >= 0 && s[i]!= ' ')
    {
        length++;
        i--;
    }
    printf("%d", length);
    return length;
}
int main(){
    char s[10000];
    fgets(s, 10000, stdin);
    lengthOfLastWord(s);
    return 0;
}