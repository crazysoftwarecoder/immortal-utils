#!/bin/bash

for i in $ `seq 1 4`; # Increase the 10 to 2x the number of cores if you want it done quicker.
do
        dd if=/dev/urandom | bzip2 -9 >> /dev/null&
done

sleep 100

pkill -f dd
