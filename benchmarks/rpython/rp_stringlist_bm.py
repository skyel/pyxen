#!/usr/bin/env python
# -*- coding: utf-8 -*-


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
def boot(argv):
    count = int(argv[1])
    table = [range(count) for i in range(count)]
    a().main(table)
    return 0;

def target(driver,args):
    return boot,None

