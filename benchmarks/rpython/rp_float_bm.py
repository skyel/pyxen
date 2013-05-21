#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import sin, cos, sqrt
import time

class Point(object):

    def __init__(self, i):
        self.x = x = sin(i)
        self.y = cos(i) * 3
        self.z = (x * x) / 2

    def __repr__(self):
        return "<Point: x=%s, y=%s, z=%s>" % (self.x, self.y, self.z)

    def normalize(self):
        x = self.x
        y = self.y
        z = self.z
        norm = sqrt(x * x + y * y + z * z)
        self.x = self.x / norm
        self.y = self.y / norm
        self.z = self.z / norm

    def maximize(self, other):
        self.x = self.x if self.x > other.x else other.x
        self.y = self.y if self.y > other.y else other.y
        self.z = self.z if self.z > other.z else other.z
        return self


def maximize(points):
    next = points[0]
    for p in points[1:]:
        next = next.maximize(p)
    return next

def benchmark(n):
    points = [None] * n
    for i in xrange(n):
        points[i] = Point(i)
    for p in points:
        p.normalize()
    return maximize(points)

POINTS = 10000000

def rp_float_main(n):
    # XXX warmup
    print "==Floating point benchmark=="
    iterations=int(n)
    for i in xrange(iterations):
        t0 = time.time()
        o = benchmark(POINTS)
        tk = time.time()
        print str(i) + ": " + str(tk-t0)
    return 0

"""
Test the performance of the Float benchmark
"%prog [options]"
"""
def boot(n):
    rp_float_main(n)

