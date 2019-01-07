#-*- coding:utf-8 -*-

from stack_1 import Stack

def par_check(symbol_string):
    balanced = True
    stack = Stack()
    index = 0
    while index < len(symbol_string) and balanced:
	symbol = symbol_string[index]
        if symbol in "({[":
	    stack.push(symbol)
        else:
	    if stack.is_empty():
	        balanced = False
	    else:
	        stack.pop()
	index = index+1
    if balanced and stack.is_empty():
	return True
    else:
	return False

print par_check("((()))")
print par_check("[[([]")

