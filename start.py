import tkinter
from tkinter import *
import subprocess
import json
import time
from fetchData import Fetch

URL = 'https://cricscore-api.appspot.com/csa'
IPL_TEAMS = ['Delhi Daredevils', 'Gujarat Lions', 'Kings XI Punjab',
             'Kolkata Knight Riders', 'Mumbai Indians', 'Rising Pune Supergiant',
             'Royal Challengers Bangalore', 'Sunrisers Hyderabad']
TEAM_IDS = []
TIME_INTERVAL = 5   #in seconds

root = Tk()
w = Label(root, text="Welcome to IPL.")
w1 = Label()
w2 = Label()
w.pack()
w1.pack()
w2.pack()
	
def get_data(url) :
    req_obj = Fetch(url)
    ret_data = req_obj.get_data()
    if ret_data is not None:
        return json.loads(ret_data)				

def get_ipl_ids() :
	for match in get_data(URL) :
		if match['t1'] in IPL_TEAMS :
			TEAM_IDS.append(match['id'])
	print TEAM_IDS

def draw() :
	for ids in TEAM_IDS:
		for match_data in get_data(URL + '?id=' + str(ids)):
			if 'Match over' not in match_data['de'] and 'match' not in match_data['de']:
				#print 'running...'
				summary = match_data['si']
				current = match_data['de']
				w1.config(text='SUMMARY : '+overall)
				w2.config(text='SCORE : '+current)
				root.after(1000,draw)

if __name__ == '__main__':
	get_ipl_ids()
	draw()
	root.mainloop()
