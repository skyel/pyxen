#!/usr/bin/env python

"""Microbenchmark for function call overhead.

This measures simple function calls that are not methods, do not use varargs or
kwargs, and do not use tuple unpacking.

This is taken from the pypy benchmarks and adapted for the pyxen project.
"""

# Python imports
import time

class rp_call_bm:

	def __init__(self):
		pass

	@staticmethod
	def foo(a, b, c, d):
	    # 20 calls
	    rp_call_bm.bar(a, b, c)
	    rp_call_bm.bar(a, b, c)
	    rp_call_bm.bar(a, b, c)
	    rp_call_bm.bar(a, b, c)
	    rp_call_bm.bar(a, b, c)
	    rp_call_bm.bar(a, b, c)
	    rp_call_bm.bar(a, b, c)
	    rp_call_bm.bar(a, b, c)
	    rp_call_bm.bar(a, b, c)
	    rp_call_bm.bar(a, b, c)
	    rp_call_bm.bar(a, b, c)
	    rp_call_bm.bar(a, b, c)
	    rp_call_bm.bar(a, b, c)
	    rp_call_bm.bar(a, b, c)
	    rp_call_bm.bar(a, b, c)
	    rp_call_bm.bar(a, b, c)
	    rp_call_bm.bar(a, b, c)
	    rp_call_bm.bar(a, b, c)
	    rp_call_bm.bar(a, b, c)
	    rp_call_bm.bar(a, b, c)
	
	
	@staticmethod
	def bar(a, b, c):
	    # 20 calls
	    rp_call_bm.baz(a, b)
	    rp_call_bm.baz(a, b)
	    rp_call_bm.baz(a, b)
	    rp_call_bm.baz(a, b)
	    rp_call_bm.baz(a, b)
	    rp_call_bm.baz(a, b)
	    rp_call_bm.baz(a, b)
	    rp_call_bm.baz(a, b)
	    rp_call_bm.baz(a, b)
	    rp_call_bm.baz(a, b)
	    rp_call_bm.baz(a, b)
	    rp_call_bm.baz(a, b)
	    rp_call_bm.baz(a, b)
	    rp_call_bm.baz(a, b)
	    rp_call_bm.baz(a, b)
	    rp_call_bm.baz(a, b)
	    rp_call_bm.baz(a, b)
	    rp_call_bm.baz(a, b)
	    rp_call_bm.baz(a, b)
	    rp_call_bm.baz(a, b)
	
	
	@staticmethod
	def baz(a, b):
	    # 20 calls
	    rp_call_bm.quux(a)
	    rp_call_bm.quux(a)
	    rp_call_bm.quux(a)
	    rp_call_bm.quux(a)
	    rp_call_bm.quux(a)
	    rp_call_bm.quux(a)
	    rp_call_bm.quux(a)
	    rp_call_bm.quux(a)
	    rp_call_bm.quux(a)
	    rp_call_bm.quux(a)
	    rp_call_bm.quux(a)
	    rp_call_bm.quux(a)
	    rp_call_bm.quux(a)
	    rp_call_bm.quux(a)
	    rp_call_bm.quux(a)
	    rp_call_bm.quux(a)
	    rp_call_bm.quux(a)
	    rp_call_bm.quux(a)
	    rp_call_bm.quux(a)
	    rp_call_bm.quux(a)
	
	
	@staticmethod
	def quux(a):
	    # 20 calls
	    rp_call_bm.qux()
	    rp_call_bm.qux()
	    rp_call_bm.qux()
	    rp_call_bm.qux()
	    rp_call_bm.qux()
	    rp_call_bm.qux()
	    rp_call_bm.qux()
	    rp_call_bm.qux()
	    rp_call_bm.qux()
	    rp_call_bm.qux()
	    rp_call_bm.qux()
	    rp_call_bm.qux()
	    rp_call_bm.qux()
	    rp_call_bm.qux()
	    rp_call_bm.qux()
	    rp_call_bm.qux()
	    rp_call_bm.qux()
	    rp_call_bm.qux()
	    rp_call_bm.qux()
	    rp_call_bm.qux()
	
	
	@staticmethod
	def qux():
	    return time.time()
	
	
	@staticmethod
	def test_calls():
	    t0 = time.time()
	    # 40 calls
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    rp_call_bm.foo(1, 2, 3, 4)
	    t1 = time.time()
	    return t1 - t0
	
	# The number of iterations
	@staticmethod
	def rp_call_main(n):
	    print "==Mixed calls benchmark=="
	    iterations=int(n)
	    for i in xrange(iterations):
	        print str(i) + ": " + str(rp_call_bm.test_calls())
	    return 0
	@staticmethod
	def boot(n):
	    rp_call_bm.rp_call_main(n)
