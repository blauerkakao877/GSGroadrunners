#!/bin/bash

echo "Roadrunner Start um: "
date
cd /home/pi/FE_2024_WF/Work
source /home/pi/env/bin/activate
python3 Openrace_kamera.py
# python3 kamera_M.py