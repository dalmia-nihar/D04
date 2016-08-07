#!/usr/bin/env python
# HW04_ch08_ex04

# The following functions are all intended to check whether a string contains
# any lowercase letters, but at least some of them are wrong. For each
# function, describe (is the docstring) what the function actually does.
# You can assume that the parameter is a string.

# Do not merely paste the output as a counterexample into the documentation
# string, explain what is wrong.

###############################################################################
# Body


def any_lowercase1(s):
    """Explain what is wrong, if anything, here.
    """
    for c in s:
        if c.islower():
            return True
        else:
            return False
    """
    Incorrect: Whatever is the first char in the string will only be checked. 
    """

def any_lowercase2(s):
    """Explain what is wrong, if anything, here.
    """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
    """
    There are 2 issues in the code: 
    1. We are calling 'c'.islower passes the char 'c' always and not the variable c
    2. The return statements are in string format whereas Boolean is expected
    """

def any_lowercase3(s):
    """Explain what is wrong, if anything, here.
    """
    for c in s:
        flag = c.islower()
    return flag
    """
    Incorrect: The case of the last char will only be checked.
    """



def any_lowercase4(s):
    """Explain what is wrong, if anything, here.
    """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag
    """
    This should work fine!  
    """

def any_lowercase5(s):
    """Explain what is wrong, if anything, here.
    """
    for c in s:
        if not c.islower():
            return False
    return True
    """
    Will only output True when ALL characters are lower case, which is not we're looking at. 
    """
###############################################################################

def main():
    # Remove print("Hello World!") and for each function above that is wrong,
    # call that function with a string for which the function returns
    # incorrectly.
    # ex.: any_lowercase_("thisstringmessesupthefunction")
    print(any_lowercase1("AbC"))
    print(any_lowercase1("abC"))
    print(any_lowercase2("ABC"))
    print(any_lowercase3("AbC"))
    print(any_lowercase3("ABc"))
    print(any_lowercase4("AbC"))
    print(any_lowercase4("Abc"))
    print(any_lowercase5("abc"))
    print(any_lowercase5("AbC"))


if __name__ == '__main__':
    main()
