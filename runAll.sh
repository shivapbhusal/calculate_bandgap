# Script to all script for all the files in a folder. 

for entry in $1/*
do 
	echo $entry;
	python compute_allGap_robust.py $entry	

done
