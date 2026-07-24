#!/bin/bash

a=`df | grep mapper | awk '{print $5}'`

echo "A partição principal ocupa $a do espaço total disponivel"
