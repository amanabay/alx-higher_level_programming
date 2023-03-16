#!/usr/bin/python3

def roman_to_int(roman_string):
    roman_numerals = {"I": 1,
                      "V": 5,
                      "X": 10,
                      "L": 50,
                      "C": 100,
                      "D": 500,
                      "M": 1000}
    number = 0
    rlist = []
    for i in range(len(roman_string)):
        if roman_string[i] in roman_numerals:
            rlist.append(roman_string[i])

    for i in range(len(rlist)):
        if i > 0 and roman_numerals[rlist[i]] > roman_numerals[rlist[i - 1]]:
            number += roman_numerals[rlist[i]] - 2 *\
                    roman_numerals[rlist[i - 1]]
        else:
            number += roman_numerals[rlist[i]]

    return number
