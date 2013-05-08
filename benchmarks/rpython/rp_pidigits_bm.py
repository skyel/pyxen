# this cannot be fully converted since we don't have full support for big numbers
# and some values will be mismatched since n becomes extremely large
import time

def pidigits(length):
    result = []
    to_ret = ""
    i = k = ns = 0
    k1 = 1
    n,a,d,t,u = 1,0,1,0,0
    while(True):
        k = k + 1
        t = n<<1
        n = n * k
        a = a + t
        k1 = k1 + 2
        a = a * k1
        d = d * k1
        if a >= n:
            t = ((n*3 + a) // d)
            u = ((n*3 + a) % d)
            u = u + n
            if d > u:
                ns = ns*10 + t
                i = i + 1
                result.append(int(t))
                if i % 10 == 0:
                    ns = 0
                if i >= length:
                    break
                a = a - d*t
                a = a * 10
                n = n * 10
    return result

def main(n, digits):
    l = []
    for i in xrange(n):
        t0 = time.time()
        print pidigits(digits)
        l.append(time.time() - t0)
    return l


# Test the pidigit calculation performance 
#     We add the number of digits as argument to prevent the rpython translator from precomputing the result
def boot(argv):
    count = int(argv[1])
    digits = int(argv[2])
    print main(count, digits)
    return 0;

def target(driver,args):
    return boot,None

main(10,15)
