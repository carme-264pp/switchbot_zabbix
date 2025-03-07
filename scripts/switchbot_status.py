import sys
import json
import requests
from switchbot_lib import *

API_URL = 'https://api.switch-bot.com/v1.1/devices/{}/status'

if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise Exception("args error: config.ini <deviceID>")
    config = loadConfig(sys.argv[1])
    config['device_id'] = sys.argv[2]

    request_url = API_URL.format(config['device_id'])
    request_headers = createAPIRequestHeaders(config['token'], config['secret'])

    with requests.get(request_url, headers=request_headers) as res:
        if res.status_code != 200:
            sys.stderr.writelines("status code: {}".format(res.status_code))
            sys.exit(-1)
        print(json.dumps(res.json()))
