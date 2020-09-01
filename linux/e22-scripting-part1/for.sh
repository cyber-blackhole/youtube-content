#!/bin/bash


for (( i=1 ; i < 5 ; i++ ))
do
	for (( j=1 ; j < 5 ; j++ ))
	do
		printf "${i}${j} \t"
	done
	printf "\n"
done
