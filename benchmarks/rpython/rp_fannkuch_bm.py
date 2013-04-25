# -*- coding: utf-8 -*-
# The Computer Language Benchmarks Game
# http://shootout.alioth.debian.org/
#
#
# contributed by Sokolov Yura
# modified by Tupteq


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
    return 0
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
def main(n):
    for i in xrange(n):
        fannkuch(DEFAULT_ARG)

def boot(arg):
#	Here we should time the run times
    main(10)
    return 0

def target(driver,args):
    description="Test the performance of the Float benchmark"
    return boot,None
