import sys
import json
import requests
from switchbot_lib import *

API_URL = 'https://api.switch-bot.com/v1.1/devices/'

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise Exception("args error: config.ini")
    config = loadConfig(sys.argv[1])

    request_headers = createAPIRequestHeaders(config['token'], config['secret'])

    with requests.get(API_URL, headers=request_headers) as res:
        if res.status_code != 200:
            sys.stderr.writelines("status code: {}".format(res.status_code))
            sys.exit(-1)
        print(json.dumps(res.json()['body']['deviceList'], indent=2))
