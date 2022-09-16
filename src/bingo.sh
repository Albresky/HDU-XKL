#!/bin/bash

echo "========================================================"
echo "[demo.py] (called) ===> " `date`

workdir="/home/XKL/src"
export PYTHONPATH=$PYTHONPATH:/usr/lib/python3/dist-package
export PATH=$PATH:${workdir}
#echo PythonPath=$PYTHONPATH
#echo path=$PATH
cd $workdir
/usr/bin/python3 ${workdir}/demo.py >> log.txt
