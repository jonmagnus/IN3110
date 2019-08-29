#!/bin/bash

declare -i tracker_running
tracker_running=0
timestamp=$(date "+%A %b %e %T %Z %Y")
echo $timestamp

function track {
	option=$1

	case "$option" in
		'start')
			if [ $tracker_running -eq 1 ] ; then
				echo 'The tracke is already running.'
				return
			else
				tracker_running=1
				timestamp=$(date "+%A %b %e %T %Z %Y")
				echo "START $timestamp" >> $LOGFILE
			fi
			if [ $# -gt 1 ] ; then
				shift
				label=$@
			else
				label='N/A'
			fi
			;;
		'stop')
			if [ $tracker_running -eq 1 ] ; then 
				tracker_running=0
				timestamp=$(date "+%A %b %e %T %Z %Y")
				echo "LABEL $label" >> $LOGFILE
				echo "STOP $timestamp" >> $LOGFILE
				echo >> $LOGFILE
				
			else
				echo 'Found no tracker running.'
			fi
			;;
		'status')
			if [ $tracker_running -eq 1 ] ; then
				echo "There is a tracker running with label '${label}' started at time ${timestamp}."
			else 
				echo "Found no tracker running."
			fi
			;;
	esac
}


rm $LOGFILE
echo "Start track"
track 'start' 123
echo "Stop track"
track 'stop'
track start
track status
track stop
cat tracker.log
