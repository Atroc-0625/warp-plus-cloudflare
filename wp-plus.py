import urllib.request
import json
import datetime
import random
import string
import time

referrer = "4bb37cb0-9f5e-407f-aea3-eef100951c31"# 群主
#referrer = "7a593954-e665-47f3-b8d9-3107c5254234"
try_time = 18


def genString(stringLength):
    try:
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for i in range(stringLength))
    except Exception as error:
        print(error)


def digitString(stringLength):
    try:
        digit = string.digits
        return ''.join((random.choice(digit) for i in range(stringLength)))
    except Exception as error:
        print(error)


url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'


def run():
    try:
        install_id = genString(22)
        body = {"key": "{}=".format(genString(43)),
                "install_id": install_id,
                "fcm_token": "{}:HELLO{}".format(install_id, genString(134)),
                "referrer": referrer,
                "warp_enabled": False,
                "tos": datetime.datetime.now().isoformat()[:-3] + "+02:00",
                "type": "Android",
                "locale": "es_ES"}
        data = json.dumps(body).encode('utf8')
        headers = {'Content-Type': 'application/json; charset=UTF-8',
                   'Host': 'api.cloudflareclient.com',
                   'Connection': 'Keep-Alive',
                   'Accept-Encoding': 'gzip',
                   'User-Agent': 'okhttp/3.12.1'
                   }
        req = urllib.request.Request(url, data, headers)
        response = urllib.request.urlopen(req)
        status_code = response.getcode()
        return status_code
    except Exception as error:
        print(error)


g = 0
b = 0
while True:
    result = run()
    if result == 200:
        g = g + 1
        print(f"\n[-] 你ID: {referrer}")
        print(f"\n[:] {g} GB 你已经刷到了")
        print(f"[#] Total: {g} Good {b} Bad")
        print(f"[*] {try_time}s之后再来一个G")
        time.sleep(try_time)
    else:
        b = b + 1
        print(f"开始出错了，60s之后重试")
        print(f"[#] Total: {g} Good {b} Bad")
        time.sleep(60)
        while True:
            again = run()
            if again == 200:
                g = g + 1
                print(f"[#] Total: {g} Good {b} Bad")
                time.sleep(try_time + 2)
            else:
                print(f"还是不行，给你退了吧")
                break
