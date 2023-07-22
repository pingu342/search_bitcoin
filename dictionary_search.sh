#!/bin/bash
cat $1 | while read line
do
  echo -n $line | ./getaddressbalance.sh
  echo
done
