#!/bin/bash

function climb {
	declare -i counter
	counter=$1
	if [ "$counter" -eq "0" ]; then
		counter=1
	fi
	declare -i i; i=0
	while [ "$i" -lt "$counter" ]; do
		cd ..
		((i++))
	done
}
