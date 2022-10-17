#!/bin/bash

echo "[demo.py] (called) ===> " `date`

workdir="/home/XKL/src"
thisPython="/usr/bin/python3"
thisPythonPATH="/usr/lib/python3/dist-package"
logFile="/home/XKL/log.txt"

export PYTHONPATH=$PYTHONPATH:${thisPythonPATH}
export PATH=$PATH:${workdir}

cd $workdir

echo "┌+==============================+┐" >> $logFile
${thisPython} ${workdir}/demo.py >> $logFile
echo `date` >> $logFile
echo "└+==============================+┘" >> $logFile

