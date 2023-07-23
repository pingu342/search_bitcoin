#!/bin/bash
cat $1 | while read line
do
  echo -n $line | ./getkeybalance.sh $2
  echo
done
