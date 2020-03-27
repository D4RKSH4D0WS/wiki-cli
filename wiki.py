#!/usr/bin/python
# -*- coding: utf-8 -*-
#Author D4RK5H4D0W5
#Rikod? boleh asal jgn apus author ya kampank
G0 = "\033[0;32m"
G1 = "\033[1;32m"
C0 = "\033[0;36m"
C1 = "\033[1;36m"
P0 = "\033[0;35m"
P1 = "\033[1;35m"
W0 = "\033[0;37m"
W1 = "\033[1;37m"
B0 = "\033[0;34m"
B1 = "\033[1;34m"
R0 = "\033[0;31m"
R1 = "\033[1;31m"
Y1 = "\033[1;33m"
Y0 = "\033[0;33m"
try:
	import requests,time,os
	from bs4 import BeautifulSoup as bs
except:
	os.system('pip2 install requests bs4')
	print("%s[%s!%s] %sRun again\n%s[%s!%s] %spython2 wiki.py"%(W1,R1,W1,W0,W1,R1,W1,W0))
	exit()
def logo():
	os.system('clear')
	print '''
%s  ___ ___ %s__ __    __          __ __
%s |   Y   |%s__|  |--|__|   .----|  |__|
%s |.  |   |%s  |    <|  |   |  __|  |  |
%s |. / \  |%s__|__|__|__|   |____|__|__|
%s |:      |
 |::.|:. | %sPowered [ wikipedia.org ]
%s `--- ---'
'''%(G1,W1,G1,W1,G1,W1,G1,W1,G1,W1,G1)
def wiki(isi):
	a=requests.get('https://id.m.wikipedia.org/w/index.php?search='+isi+'&title=Istimewa%3APencarian&profile=default&fulltext=1&ns0=1')
	b=bs(a.content,'html.parser')
	c=b.find_all('div',class_='searchresult')[0]
	print '%s[%s>%s] %sResult: %s'%(G1,Y1,G1,W1,c.text)
	exit()
def main():
	logo()
	isi = raw_input('\033[1;32m[\033[1;33m?\033[1;32m]\033[1;37m Masukkan kata: ')
	if isi == '':
		print('%s[%s!%s] %sJangan kosong cok'%(W1,R1,W1,W0))
		time.sleep(0.8)
		main()
	wiki(isi)
if __name__=='__main__':
	main()
