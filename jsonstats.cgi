#!/bin/bash
# New CGI that presents stats as JSON
# Author: Thran Authored: 06/12/19
source common.sh

testFlag="/tmp/.testrunning"
lastMsg="/tmp/.lastmsg"
# Sample uses nginx, edit to print stats of any process name
procName="nginx"

writeJSONHeader

# CPU Usage in tenths of a percent
function getProcCPU {
    ps --no-headers -C $procName -o cp | awk '{cp += $1} END {print cp}'
}
# PS returns perc of CPU time / time program has been running.
function getProcCPUPerc {
    ps --no-headers -C $procName-o %cpu | awk '{cpu += $1} END {print cpu}'
}

function getUptime {
    uptime -p | sed 's/up //' | sed 's/utes//' | tr -d '\n' 
}

function getTotalMem {
    free -m | grep Mem | awk '{ print $3 }' | tr -d '\n'
}

function getLoadAvg {
    uptime |  awk -F 'load average:' '{ print $2 }' | tr -d ',' | tr -d '\n'
}

# Resident set size; total of process in memory
function getProcRSS {
    local rss=$( ps --no-headers -C "$1" -o rss |  awk '{rss += $1} END {print rss}' )
    if [ -z $rss ]; then
        echo "0"
    else
        echo $rss
    fi
}

function isTestRunning {
   if [ -e "$testFlag" ]; then
        echo "true"
   else
        echo "false" 
   fi
}

function getLastMsg {
    if [ -s "$lastMsg" ]; then
        cat "$lastMsg"
    else
        echo "$(date): No status yet..."
    fi
}

# Begin JSON composition
echo "{"

jT "uptime"
jF "$(getUptime)"

jT "totalMem"
jF "$(getTotalMem)"

jT "loadAvg"
jF "$(getLoadAvg)"

jT "nginxCPU"
jF "$(getProcCPU)" 

jT "nginxCPUPerc"
jF "$(getProcCPUPerc)" 

jT "nginxRssKb"
jF "$(getProcRSS $procName )"

jT "ffmpegRssKb"
jF "$(getProcRSS ffmpeg )"

jT "isTestRunning"
jF "$(isTestRunning)" 

jT "lastMsg"
jF "$(getLastMsg)" "f" # don't forget the 'f' param to flag last field

echo "}"
