#!/bin/bash

declare -i tracker_running
tracker_running=0

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
		'log')
			declare -i s_time d_time
			s_time=0
			for line in $(cat ${LOGFILE} | sed "s/ /SUBSTITUTE/g"); do
				#echo pre line $line
				line=$(echo $line | sed "s/SUBSTITUTE/ /g")
				#echo post line $line
				case "$(echo $line | cut -d " " -f 1)" in
					'START')
						s_time="$(echo $line | \
							cut -d " " -f 5 | \
							xargs date +%s -d)"
						;;
					'LABEL')
						log_label="$(echo $line | \
							cut -d " " --complement -f 1)"
						;;
					'STOP')
						d_time=$(("$(echo $line | \
							cut -d " " -f 5 | \
							xargs date +%s -d)" \
							- ${s_time}))
						echo "${log_label} : $(date +%H:%M:%S -ud @${d_time})"
						;;
				esac
			done
			
			# A nice bonus ;)
			if [ ${tracker_running} -eq 1 ] ; then
				echo "${label} : $(date +%H:%M:%S -ud @$(($(date +%s) - ${s_time})))"
			fi
			;;
	esac
}
