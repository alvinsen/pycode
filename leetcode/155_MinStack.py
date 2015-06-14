#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
"""
Min Stack
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Stack: 后进先出
push：在最顶层加入数据。
pop：返回并移除最顶层的数据。
top：返回最顶层数据的值，但不移除它。
isempty：返回一个布尔值，表示当前stack是否为空栈。

class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        if len(self.minStack) == 0 or self.minStack[-1] >= x:
            #print 'minn change'
            self.minStack.append(x)
 
    # @return nothing
    def pop(self):
        p = self.stack.pop()
        #print 'pop ' , p
        if p == self.minStack[-1]:
            #print 'minn pop'
            self.minStack.pop()

    # @return an integer
    def top(self):
        return self.stack[-1]

    # @return an integer
    def getMin(self):
        return self.minStack[-1]

"""
class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
        #self.minStack.append(0)

    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        if len(self.minStack) == 0 or self.minStack[-1][0] > x:
            #print 'minn change'
            self.minStack.append((x,1))
        elif x == self.minStack[-1][0]:
            self.minStack[-1] = (x, self.minStack[-1][1] + 1)

    # @return nothing
    def pop(self):
        p = self.stack.pop()
        #print 'pop ' , p
        if p == self.minStack[-1][0]:
            if self.minStack[-1][1] > 1:
                #print 'minn pop'
                self.minStack[-1] = (self.minStack[-1][0], self.minStack[-1][1] - 1)
            else:
                self.minStack.pop()

    # @return an integer
    def top(self):
        return self.stack[-1]

    # @return an integer
    def getMin(self):
        #print self.minStack
        return self.minStack[-1][0]

if __name__ == '__main__':
    
    stk = MinStack()
    for i in range(-10000, 60000):
        stk.push(i)

    # import pdb;pdb.set_trace()
    # skt.minStack

    # for i in range(10000):
    #     m = skt.getMin()
    #     print 'min: %s' %m
    #     skt.pop()


