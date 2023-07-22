#!/bin/bash
N=$1
while true
do
  str=`pwgen $N -n 1`
  echo $str | ./getaddressbalance.sh
  echo 
  sleep 0.1
done
