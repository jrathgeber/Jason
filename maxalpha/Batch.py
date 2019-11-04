# -*- coding: utf-8 -*-

import os;
import RightEdge as RE;
import MaxAlpha as MA;
import time;
import sendMail;
import SymbolConfig as SC;
import threading;
import configparser
import Tweet

config = configparser.ConfigParser()
config.read('C:\etc\properties.ini') 

gdurl = config['godaddy']['godaddy.url']
gduser = config['godaddy']['godaddy.user']
gdpass = config['godaddy']['godaddy.pass']

url = config['yahoo']['yahoo.url']
user = config['yahoo']['yahoo.user']
password = config['yahoo']['yahoo.pass']
server = config['yahoo']['yahoo.server']
port = config['yahoo']['yahoo.port']
username = config['yahoo']['yahoo.username']

os.chdir('C:\\dep\Mechanizd\\maxalpha\\')

daterun = time.strftime("%Y%m%d")

#print(daterun)

closeup = '/E'
get_prices = '/U'
#get_prices = ''
mode = '/L'

#maxdata=["The", "earth", "revolves", "around", "sun"]
maxdata='hello'


def MyThread1():
    RE.runRightEdge('MaxAlphaLive', 'MaxAlpha', 'MaxAlpha', mode, '/'+ daterun, get_prices, closeup)
   
    
#tickerList = ['AXSM', 'VIPS']    
tickerList = MA.parseWebSite(daterun);

print(tickerList)

if tickerList[0]=='error':
    sendMail.send_mail('jrathgeber@yahoo.com', 'jrathgeber@yahoo.com', 'Max List Eorror ' + ''.join(tickerList), ''.join(tickerList), [], server, port, username, password)
else:
    SC.getSymbolConfig(tickerList, daterun, maxdata)
    sendMail.send_mail(user, user, 'Max ' + ','.join(tickerList), ', $'.join(tickerList),[], server, port, username, password)
    Tweet.tweetSomething('Day Trading Watchlist $' + ', $'.join(tickerList))
    t1 = threading.Thread(target=MyThread1)
    t1.start()

#    
