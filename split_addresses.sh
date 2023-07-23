#!/bin/bash
split -l 5000000 $1 $1.splitted-
for FILE in $1.splitted-*; do
  sort <$FILE >sorted-$FILE &
done
wait
sort -m sorted-$1.splitted-* >sorted-$1
rm $1.splitted-*
rm sorted-$1.splitted-*
split -l 50000 -a 3 sorted-$1 sorted-$1.splitted-
rm sorted-$1
