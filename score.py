import subprocess
import json
import time
from fetchData import Fetch

URL = 'https://cricscore-api.appspot.com/csa'
IPL_TEAMS = ['Delhi Daredevils', 'Gujarat Lions', 'Kings XI Punjab',
             'Kolkata Knight Riders', 'Mumbai Indians', 'Rising Pune Supergiant',
             'Royal Challengers Bangalore', 'Sunrisers Hyderabad']
TIME_INTERVAL = 60   #in seconds


def get_data(url):
    req_obj = Fetch(url)
    ret_data = req_obj.get_data()
    if ret_data is not None:
        return json.loads(ret_data)

if __name__ == '__main__':
    while True:
        for match in get_data(URL):
            if match['t1'] in IPL_TEAMS:
                for match_data in get_data(URL + '?id=' + str(match['id'])):
                    if 'Match over' not in match_data['de']:
                        subprocess.Popen(['notify-send', match_data['de']])
                        time.sleep(TIME_INTERVAL)
