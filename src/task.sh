#!/bin/bash

echo "[demo.py] (called) ===> " `date`

workdir="/home/XKL/src"
thisPython="/usr/bin/python3"
thisPythonPATH="/usr/lib/python3/dist-package"

export PYTHONPATH=$PYTHONPATH:${thisPythonPATH}
export PATH=$PATH:${workdir}

cd $workdir
echo "┌+==============================+┐" >> log.txt
${thisPython} ${workdir}/demo.py >> log.txt
echo `date` >> log.txt
echo "└+==============================+┘" >> log.txt

