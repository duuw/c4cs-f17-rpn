#!/usr/bin/env python3
import operator
import readline
import sys
from termcolor import colored, cprint

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow
}

def calculate(string):
    stack = list()
    for token in string.split():
        try:
            stack.append(int(token))
        except ValueError:
            arg2 = stack.pop()
            arg1 = stack.pop()
            function = ops[token]
            result = function(arg1, arg2)
            stack.append(result)
    print(stack)
    res = stack.pop()
    if res < 0:
        print(colored(res, 'red', attrs=['bold']))
    else:
        print(colored(res, 'white', attrs=['bold']))
            
def main():
    while True:
        userInput = input("rpn calc> ")
        if userInput == 'quit':
             print("thanks for using rpn calc")
             exit()
        else:
             calculate(userInput)

if __name__ == '__main__':
    main()

