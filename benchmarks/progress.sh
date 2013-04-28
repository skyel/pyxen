#!/bin/bash

echo "Current translation progress:"

stat pure-python  &> /dev/null
script_ok=$?
if [ $? -ne 0 ]
then
	echo "Could not find ./pure-python"
	exit 1
fi

rm -f ./pure-python/*.pyc

stat rpython &> /dev/null
if [ $? -ne 0 ]
then
	echo "Could not find ./rpython"
	exit 1
fi
rm -f ./rpython/*.pyc

pure_total=`ls -l ./pure-python | grep -i .py | wc -l`
rpython_total=`ls -l ./rpython | grep -i .py | wc -l`

echo $rpython_total/$pure_total

