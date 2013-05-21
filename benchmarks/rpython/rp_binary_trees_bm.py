# -*- coding: utf-8 -*-
# The Computer Language Benchmarks Game
# http://shootout.alioth.debian.org/
#
# contributed by Antoine Pitrou
# modified by Dominique Wahli and Daniel Nanz
#
# Ported to RPython by Razvan Ghitulete

import sys
import time

"""
We use this class due to the fact that RPython
does not allow list to contain different types of
objects. Hence this is one of the simplest ways
to represent the tree
"""
class Node(object):
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def getVal(self):
        return self.value

    def getL(self):
        return self.left

    def getR(self):
        return self.right


def make_tree(i=int, d=int):

    if d > 0:
        i2 = i + i
        d -= 1
        return Node(i, make_tree(i2-1,d), make_tree(i2,d));
    x = Node(0,None,None)
    return Node(i, x, x);


def check_tree(node):

    i = node.getVal();
    l = node.getL();
    r = node.getR();
    if l is None:
        return i
    else:
        return i + check_tree(l) - check_tree(r)


def make_check(itde, make=make_tree, check=check_tree):

    i, d = itde
    return check(make(i, d))


def get_argchunks(i, d, iterator, chunksize=5000):

    chunk = []
    start = iterator * (chunksize / 2) + 1
    for k in xrange(start, i + 1):
        chunk.extend([(k, d), (-k, d)])
        if len(chunk) == chunksize:
            return chunk
    return chunk


def binary_tree(n, min_depth=4):

    chunksize = 5000
    max_depth = max(min_depth + 2, n)
    stretch_depth = max_depth + 1

    print 'stretch tree of depth %d\t check: %d' % (
          stretch_depth, make_check((0, stretch_depth)))

    long_lived_tree = make_tree(0, max_depth)

    mmd = max_depth + min_depth
    for d in xrange(min_depth, stretch_depth, 2):
        i = 1
        for _ in xrange(mmd - d):
            i *= 2
        cs = 0
        for j in xrange(2 * i / chunksize + 1):
            argchunk = get_argchunks(i, d, j, chunksize)
            for x in argchunk:
                cs += make_check(x)
        print '%d\t trees of depth %d\t check: %d' % (i * 2, d, cs)


def rp_binary_tree_main(n):
    print "==Binary Trees Benchmark=="
    for i in xrange(n):
        t0 = time.time()
        binary_tree(12)
        t1 = time.time()
        print str(i) + ": " + str(t1-t0)
    return 0;

def boot(n):
    rp_binary_tree_main(n)

