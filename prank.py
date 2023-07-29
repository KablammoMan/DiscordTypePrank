import requests
import time

headers = {
    'Authorization': 'auth-token-here',
}

channelid = input("Channel ID: ")
timei = int(input("Time (s): "))

start = time.time()
while time.time() - start < timei:
    response = requests.post('https://discord.com/api/v9/channels/' + channelid +'/typing', headers=headers)
    time.sleep(5)
