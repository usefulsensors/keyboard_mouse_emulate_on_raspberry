#!/usr/bin/bash -xe

cd -- "$( dirname -- "${BASH_SOURCE[0]:-$0}"; )"

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

python3 -u server/input_agent2.py 2>&1 >/tmp/input_agent_log.txt &

sudo python3 -u server/btk_server.py 2>&1 >/tmp/bt_server_log.txt &
