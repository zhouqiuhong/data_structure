# -*- coding:utf-8 -*-
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
	self.items.append(item)

    def pop(self):
	return self.items.pop()

    def peek(self):
	return self.items[len(self.items)-1]

    def is_empty(self):
	return self.items == []


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push("HOHO")
#    print stack.peek()

