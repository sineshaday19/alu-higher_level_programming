#!/usr/bin/python3
'''
Defines indentation function that indents text
'''


def text_indentation(text):
    '''
    Function that prints text with two new lines
    after each of these characters ., ? and :

    Args:
       text (str): The string to be printed
    '''
    if not(isinstance(text, str)):
        raise TypeError("text must be a string")

    i = 0
    while(i < len(text) and text[i] == ' '):
        i += 1

    while i < len(text):
        print(text[i], end="")
        if text[i] == "\n" or text[i] in ".?:":
            if text[i] in ('.', '?', ':'):
                print('\n')
            i += 1
            while(i < len(text) and text[i] == ' '):
                i += 1
            continue
        i += 1
