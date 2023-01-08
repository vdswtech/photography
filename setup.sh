#!/bin/bash

for each in */*
do
	photography.py -i $each
done

photography.py -I .

exit 0
