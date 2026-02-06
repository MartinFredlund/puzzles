#include <iostream>
#include <string>
using namespace std;

int main()
{
    string fileName;
    getline(cin, fileName);
    size_t pos = fileName.rfind(".");
    string ending = fileName.substr(pos);
    cout << ending;
}