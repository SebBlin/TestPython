#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# * Program de test

from collections import deque

def fib(n):    # write Fibonacci series up to n
     """Print a Fibonacci series up to n."""
     a, b = 0, 1
     while a < n:
         print(a, end=' ')
         a, b = b, a+b
     print ()

def enq(n):
	stack = []
	for c in range(n):
		stack.append(c)
		print(stack)
	queue = deque(stack)
	while queue:
		queue.popleft()
		print (list(queue))
		
		 
enq(100)