# switchbot_zabbix

## Install

1. Setup Python enviroment

   ```shell
   cd switchbot_zabbix/
   python -m venv env
   source ./env/bin/activate
   pip install -r requirements.txt
   ```

2. Copy zabbix config

   ```shell
   sudo cp switchbot_zabbix/zabbix/switchbot.conf /etc/zabbix/zabbix_agent2.d/
   sudo systemctl restart zabbix-agent2.service
   ```

3. Import zabbix template

   Import zabbix/switchbot_monitor_template.yaml


## Setup

1. Get Switchbot API token

   Reference URL: https://github.com/OpenWonderLabs/SwitchBotAPI?tab=readme-ov-file#getting-started

2. Set the token in your config file
   ```ini
   [switchbot.api]
   token = <token>
   secret = <secret>
   ```

3. Get the device ID

   ```shell
   python scripts/switchbot_devices.py ./switchbot_config.ini
   [
     {
       "deviceId": "xxxxxxxxxxxx",   # Save this value
       "deviceName": "Meter",
       "deviceType": "Meter",
       "enableCloudService": true,
       "hubDeviceId": "xxxxxxxxxxxx"
     },
     {
       "deviceId": "xxxxxxxxxxxx",   # Save this value
       "deviceName": "Hub 2",
       "deviceType": "Hub 2",
       "enableCloudService": true,
       "hubDeviceId": "000000000000"
     }
   ]
   ```

4. Create a host in zabbix

   - Templates -> SwitchBot Monitor
   - Interface
     - Type       -> Agent
     - IP Address -> The IP address of the server where the script is installed
   - Macro
     - {$CONFIG_PATH} -> config file path
     - {$DEVICE_ID}   -> device ID
