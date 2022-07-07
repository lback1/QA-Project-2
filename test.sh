#!/bin/bash

declare -a dirs=(service1 service2 service3 service4)

for dir in ${dirs[@]}; do
  cd ${dir}
  sudo apt update
  sudo apt upgrade
  sudo apt install python3 python3-venv python3-pip
  python3 -m venv venv
  source venv/bin/activate
  pip3 install -r requirements.txt
  python3 -m pytest --cov=application --cov=report=html
  deactivate
  cd ..
done