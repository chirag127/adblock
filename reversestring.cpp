

// Reverse the list of the string formated as newline separated

#include <iostream>
#include <string>

main()
{
    std::string str;
    std::string rev;
    std::getline(std::cin, str);
    for (int i = str.length() - 1; i >= 0; i--)
    {
        rev += str[i];
    }
    std::cout << rev << std::endl;
}
