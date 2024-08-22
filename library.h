/**
 * @brief Doc at the start of the h file
 */

#ifndef AUTO_DOC_EXAMPLE_LIBRARY_H
#define AUTO_DOC_EXAMPLE_LIBRARY_H

/// Different comment in h file
void hello();

/// Some commented class
class SomeClass{
public:
    /// @brief Public property
    int pub;
    int not_commented;

    /// Comment in the h file
    /// @param a First param
    /// @param b Second param
    /// @param c Third param
    int commented(int a, int b, void* c);

    char comment_in_c_file(int a);

    /*
     * Comment in h file
     * @param b Param b
     */
    char comment_in_h_file(int b);

    void no_comment();
protected:
    /// protected property
    int prot;
private:
    /// Private property
    int priv;
};


#endif //AUTO_DOC_EXAMPLE_LIBRARY_H
