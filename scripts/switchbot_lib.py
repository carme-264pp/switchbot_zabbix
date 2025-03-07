import os
import configparser
import time
import hashlib
import hmac
import base64
import uuid

INI_SECTION = 'switchbot.api'

def createAPIRequestHeaders(token: str, secret: str) -> dict[str]:
    nonce = uuid.uuid4()
    t = int(round(time.time() * 1000))
    string_to_sign = '{}{}{}'.format(token, str(t), nonce)

    string_to_sign = bytes(string_to_sign, 'utf-8')
    secret = bytes(secret, 'utf-8')
    sign = base64.b64encode(hmac.new(secret, msg=string_to_sign, digestmod=hashlib.sha256).digest())

    request_headers = {}
    request_headers['Authorization'] = token
    request_headers['Content-Type'] = 'application/json'
    request_headers['charset'] = 'utf8'
    request_headers['t'] = str(t)
    request_headers['sign'] = str(sign, 'utf8')
    request_headers['nonce'] = str(nonce)

    return request_headers

def loadConfig(ini_filepath: str) -> dict[str]:
    if not os.path.exists(ini_filepath):
        raise FileNotFoundError("file not found: {}".format(ini_filepath))

    config_parser = configparser.ConfigParser()
    with open(ini_filepath, encoding='utf8') as ini_file:
        config_parser.read_file(ini_file)

    if INI_SECTION not in config_parser:
        raise Exception("Config error")
    if 'token' not in config_parser[INI_SECTION]:
        raise Exception("Config error")
    if 'secret' not in config_parser[INI_SECTION]:
        raise Exception("Config error")

    config = {}
    config['token'] = config_parser[INI_SECTION]['token']
    config['secret'] = config_parser[INI_SECTION]['secret']

    return config
