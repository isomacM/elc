#!/bin/bash

log="/home/philipp/counter/elc.log"
ram="/home/philipp/heater/ramdisk/elc.txt"

now=$(date '+%d.%m.%Y')
counterYesterday=`tail -1 $log|awk '{print $2}'`
counterToday=`/home/philipp/counter/sml -s /dev/ttyUSB0`
counterDiff=`echo "$counterToday-$counterYesterday"|bc`
echo "$now $counterToday $counterDiff" >> $log

echo "$counterToday" > $ram

