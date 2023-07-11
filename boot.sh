#!/usr/bin/bash -x
#Stop the background process
sudo hciconfig hci0 down
sudo systemctl daemon-reload
sudo /etc/init.d/bluetooth start
# Update  mac address
./updateMac.sh
#Update Name
./updateName.sh Caption_Box_Keyboard
#Get current Path
export C_PATH=$(pwd)

python3 server/input_agent.py 2>&1 >/tmp/input_agent_log.txt &

sudo server/btk_server.py
