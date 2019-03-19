#!/usr/bin/env python3

string = input('Enter the string you want to be spoilerized!\n')
spoilers = '||||'
liststring = list(string)
spoilerized = spoilers.join(liststring)
print('Your spoilerized string is: ||' + spoilerized + '||')
