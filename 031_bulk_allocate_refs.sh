#!/bin/bash

echo "starting bulk references allocation script"

PROCESS_FILE='match_file_path_name.xlsx'

START=0
END=18000
INTERVAL=2000

for i in $(seq $START $INTERVAL $END);
do
    python3 -m allocate_refs $PROCESS_FILE $i $((i + INTERVAL)) &
done

wait

echo "done"