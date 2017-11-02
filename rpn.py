#!/usr/bin/env python3
import operator
import readline

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
    return stack.pop()
       
def main():
    while True:
        calculate(input("rpn calc> "))

if __name__ == '__main__':
    main()

