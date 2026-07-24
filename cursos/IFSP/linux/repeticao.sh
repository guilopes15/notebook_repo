#!/bin/bash

for i in `seq 10`; do
    echo "contando... $i"
done

n=1
while ["$n" -le 10]; do
    echo "contando... $n"
    n=$(($n+1))
done
