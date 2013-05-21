# -*- coding: utf-8 -*-
# The Computer Language Benchmarks Game
# http://shootout.alioth.debian.org/
#
# modified by Ian Osgood
# modified again by Heinrich Acker

from pypy.rlib import rrandom 
import sys
import time

MAXINT = 0xffffffff
alu = (
   'GGCCGGGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGG'
   'GAGGCCGAGGCGGGCGGATCACCTGAGGTCAGGAGTTCGAGA'
   'CCAGCCTGGCCAACATGGTGAAACCCCGTCTCTACTAAAAAT'
   'ACAAAAATTAGCCGGGCGTGGTGGCGCGCGCCTGTAATCCCA'
   'GCTACTCGGGAGGCTGAGGCAGGAGAATCGCTTGAACCCGGG'
   'AGGCGGAGGTTGCAGTGAGCCGAGATCGCGCCACTGCACTCC'
   'AGCCTGGGCGACAGAGCGAGACTCCGTCTCAAAAA')

iub = zip('acgtBDHKMNRSVWY', [0.27, 0.12, 0.12, 0.27] + [0.02]*11)

homosapiens = [
    ('a', 0.3029549426680),
    ('c', 0.1979883004921),
    ('g', 0.1975473066391),
    ('t', 0.3015094502008),
]
def bis(a, x, lo=0, hi=None):

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x < a[mid]: hi = mid
        else: lo = mid+1
    return lo

def genRandom(lim, last, ia = 3877, ic = 29573, im = 139968):
    if (last == 0):
        seed = 42
    else:
        seed = last 
	randy = rrandom.Random(0)
	seed = randy.random() * MAXINT
    imf = float(im)
    seed = (seed * ia + ic) % im
    return lim * seed / imf


def makeCumulative(table):
    P = []
    C = []
    prob = 0.
    for char, p in table:
        prob += p
        P += [prob]
        C += [char]
    return (P, C)

def repeatFasta(src, n):
    res = ""
    width = 60
    r = len(src)
    s = src + src + src[:n % r]
    for j in xrange(n // width):
        i = j*width % r
        res = res + str(s[i:i+width])
    if n % width:
        var = len(s) - (n % width)
        if var < 0:
            var = 0
        res = res + str(s[var:len(s)])
    return res

def randomFasta(table, n):
    res = ""
    var = 0
    width = 60
    r = xrange(width)
    bb = bis
    gR = genRandom
    jn = ''.join
    probs, chars = makeCumulative(table)
    for j in xrange(n // width):
        res = res + jn([chars[bb(probs, gR(1.0, var))] for i in r])
    if n % width:
        res = res + jn([chars[bb(probs, gR(1.0, var))] for i in xrange(n % width)])
    return res


def fasta_boot(argv):
    n = 1337
    for _ in xrange(int(argv)):
        repeatFasta(alu, n*2)

        randomFasta(iub, n*3)

        randomFasta(homosapiens, n*5)
    return 0

def rp_fasta_main(n):
    print "==Fasta Benchmark=="
    iterations=int(n)
    for i in xrange(iterations):
        t0 = time.time()
        fasta_boot(1000)
        t1 = time.time()
        print str(i) + ": " + str(t1-t0)
    return 0

def boot(n):
    rp_fasta_main(n)

boot(1)
