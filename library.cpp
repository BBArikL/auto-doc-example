/**
 * @brief Doc at the start of the C file
 */
#include "library.h"

#include <iostream>

/// Says hello
void hello() {
    std::cout << "Hello, World!" << std::endl;
}


int SomeClass::commented(int a, int b, void *c) {
    return 0;
}

void SomeClass::no_comment() {

}

/*
 * Comment for the function
 * @param a Param a
 */
char SomeClass::comment_in_c_file(int a) {
    return 0;
}

char SomeClass::comment_in_h_file(int b) {
    return 0;
}
