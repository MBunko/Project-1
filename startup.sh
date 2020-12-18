#!/bin/bash 
sudo apt update
sudo apt-get install python3-venv
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
sudo mkdir /opt/Project
sudo chown -R jenkins /opt/Project
sudo systemctl daemon-reload
sudo systemctl stop Project-1.service
sudo systemctl start Project-1.service
