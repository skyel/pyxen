#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time

class a(object):
  def main(self, table):
    tmp = ''
    toRet = ''
    _buffer = []
    _buffer.append('<table xmlns:py="http://spitfire/">')
    _buffer.append('\n')
    for row in table:
      _buffer.append('<tr>')
      _buffer.append('\n')
      for column in row:
        _buffer.append('<td>')
        tmp = str(column)
        _buffer.append(tmp)
        _buffer.append('</td>')
        _buffer.append('\n')
      _buffer.append('</tr>')
      _buffer.append('\n')
    _buffer.append('</table>')
    _buffer.append('\n')
    for atom in xrange(len(_buffer)):
        toRet = toRet + _buffer[atom]
    return toRet

# Pass as argument square root of the number of elements in the table
def rp_stringlist_boot(argv):
    count = argv
    table = [range(count) for i in range(count)]
    a().main(table)
    return 0;

def rp_stringlist_main(n):
    print "==Stringlist benchmark=="
    iterations=int(n)
    for i in xrange(iterations):
        t0 = time.time()
        rp_stringlist_boot(2000)
        t1 = time.time()
        print str(i) + ": Time " + str(t1-t0)
    return 0
