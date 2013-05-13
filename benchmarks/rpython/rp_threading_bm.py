#!/usr/bin/env python

"""Some simple microbenchmarks for Python's threading support.

Current microbenchmarks:
    - *_count: count down from a given large number. Example used by David
               Beazley in his talk on the GIL (http://blip.tv/file/2232410). The
               iterative version is named iterative_count, the threaded version
               is threaded_count.

Example usage:
    ./bm_threading.py --num_threads=8 --check_interval=1000 threaded_count
"""

# Python imports
import sys
import time
from pypy.module.thread import ll_thread


def count(iterations=1000000):
    """Count down from a given starting point."""
    ll_thread.gc_thread_prepare()
    while iterations > 0:
        iterations -= 1


def test_iterative_count(iterations, num_threads):
    # Warm up.
    count(1000)

    times = []
    t0 = time.time()
    for _ in xrange(iterations):
        for _ in xrange(num_threads):
            count()
    t1 = time.time()
    return t1 - t0


def test_threaded_count(iterations, num_threads):
    # Warm up.
    count(1000)

    threads = []
    t0 = time.time()
    for _ in xrange(iterations):
		for _ in xrange(num_threads):
			threads.append(ll_thread.start_new_thread(count, ()))
    t1 = time.time()
    return t1 - t0

#"Test the performance of Python's threads."
#   argv[1] = benchmark call :
#                        iterative / threadead
#   argv[2] = num_threads
#   argv[3] = iterations

def rp_threading_boot(argv):
    if len(argv) != 4:
        print "incorrect number of arguments"
        return 1
    bm_name = argv[1]
    if (bm_name == "iterative"):
        func = test_iterative_count
    else:
        func = test_threaded_count
    num_threads = int(argv[2])
    iterations = int(argv[3])

    print func(iterations, num_threads)

    return 0;

def rp_threading_main(n):
    print "==Threading Benchmark=="
    iterations=int(n)
    argv = ["Ignore", "non_iterative", "100", "1"]
    for i in xrange(iterations):
        t0 = time.time()
        rp_threading_main(argv)
        t1 = time.time()
        print str(i) + ": Time " + str(t1-t0)
    return 0
