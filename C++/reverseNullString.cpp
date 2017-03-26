// Page 73 of Cracking the Coding Interview
// 1.2: Implement a function void reverse(char* str) in C or C++ which reverses a null-terminated string.

#include <iostream>
#include <string>


void revNullStr(char* inp) {
    int i = 0;
    char temp = ' ';
    std::string result = "";
    while (temp != '\0') {
        temp = inp[i];
        result = temp + result;
        i++;
        temp = inp[i];
    }
    std::cout << result << std::endl;
}

int main()
{
    char* var = "text";
    revNullStr(var);
}
