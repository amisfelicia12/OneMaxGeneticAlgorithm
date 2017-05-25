#!/bin/bash
#
# 
#
# 
#
# 
#
for (( i=0; i<30; i++ ))
do
	echo "hello $i"
	python OneMaxSimpleMutation.py > file$i.csv
	python AdvancedMutationOneMax.py > AdvFile$i.csv
done
#
# 
#
