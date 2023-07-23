#!/bin/bash
N=$1
while true
do
  str=`pwgen $N -n 1`
  echo $str | ./getkeybalance.sh $2
  echo 
  sleep 0.1
done
