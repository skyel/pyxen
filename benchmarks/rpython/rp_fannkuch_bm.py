# -*- coding: utf-8 -*-
# The Computer Language Benchmarks Game
# http://shootout.alioth.debian.org/
#
#
# contributed by Sokolov Yura
# modified by Tupteq

import time

def fannkuch(n):
    count = []
    max_flips = 0
    m = n-1
    r = n
    check = 0
    perm1 = []
    perm = []
    perm1_ins = perm1.insert
    perm1_pop = perm1.pop
    
    for i in xrange(n):
        count.insert(i,i+1)
        perm1.insert(i,i)
        perm.insert(i,i)

    while 1:
        if check < 30:
            check += 1

        while r != 1:
            count[r-1] = r
            r -= 1

        if perm1[0] != 0 and perm1[m] != m:
            perm = perm1[:]
            flips_count = 0
            k = perm[0]
            while k:
                perm[:k+1] = perm[k::-1]
                flips_count += 1
                k = perm[0]

            if flips_count > max_flips:
                max_flips = flips_count

        while r != n:
            perm1_ins(r, perm1_pop(0))
            count[r] = count[r] - 1
            if count[r] > 0:
                break
            r += 1
        else:
            return max_flips

DEFAULT_ARG = 9

# The parameter n for main is used to specify the number of runs
def rp_fannkuch_main(n):
    print "==Fannkuch Benchmark=="
    iterations=int(n)
    for i in xrange(iterations):
        t0=time.time()
        fannkuch(DEFAULT_ARG)
        t1=time.time()
        print str(i) + ": " + str(t1-t0)
    return 0

def boot(n):
    rp_fannkuch_main(n)

