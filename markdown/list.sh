#!/usr/bin/env bash


for f in `ls */ -1d`
do
    echo $f `ls $f -1 | wc -l`
done

