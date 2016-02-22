#!/usr/bin/python3

import os, sys, socket, urllib, time

# dict: conn : ip,subnet,gw,ifname,type,ssid
"""def get_current_connection() :
	conn = dict()
	subnet = 24
	ip = get_ip_address()
	conn['ip'] '/' + str(subnet)
	conn['gw'] = input()
	return 
"""

def print_conn(conn):
	print (conn['ip'],' ', conn['gw'], ' ', conn['subnet'], ' ', conn['ifname'], ' ', conn['con_type'], ' ',conn['ssid'])

def get_conn_info(conn):
	# dict: conn : ip,subnet,gw,ifname,type,ssid
	subnet = 24 # 255.255.255.0, assumed
	# read kernel routing table
	os.system("sudo route -n | grep \'UG\' | awk \'{print $2}\' > gw")
	gw_file = open("gw", "r")
	conn['gw'] = gw_file.read()
	conn['gw'] = conn['gw'].rstrip('\n')
	gw_file.close()
	os.remove("gw")
	# open a socket connection to get current ip address
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	conn['ip'] = str(s.getsockname()[0])
	s.close()
	conn['ip'] = conn['ip'] 
	conn['subnet'] = str(subnet)
	# display current GENERAL.DEVICE and GENERAL.TYPE and ask input as required
	# that is infact executed via a shell script
	os.system('bash get_ifaces.bash')
	print()
	print ("Enter the device name and type in separate lines to handle")
	conn['ifname'] = input("Device name (eg. eth0) ")
	conn['con_type'] = input("Type (eg. ethernet) ")
	print('got current connection')
	if (conn['con_type'] == 'wifi'):
		conn['ssid'] = input('Enter ssid of wifi connection: ')

'''def test_connection():
	return int( os.system('GET -d www.google.com') )
'''
'''def test_connection():
	try:
		host = socket.gethostbyname("www.google.com")
		socket.create_connection((host, 80), 2)
		return 0
	except:
		pass
	return 1
'''

def test_connection():
	os.system('wget -t 1 --quiet www.google.com')
	retvalue = os.path.exists('index.html')
	os.system('rm index.html > /dev/null')
	return retvalue


def create_connection(conn):
	# dict: conn : ip,subnet,gw,ifname,type,ssid
#	print("creating connection")
	arg = 'nmcli con add con-name new_conn ifname ' + conn['ifname'] + ' type ' + conn['con_type'] 
	if (conn['con_type'] == 'wifi'):
		arg += 'ssid ' + conn['ssid']
	arg += ' ip4 ' + conn['ip'] + '/' + conn['subnet'] + ' gw4 ' + conn['gw']
	#print (arg)
	a = os.system(arg + ' > /dev/null')
	if (a != 0):
		exit()
#	print("connection created")


def modify_connection(conn):
	arg = 'nmcli con mod new_conn +ipv4.addresses "' + conn['ip'] + '/' + conn['subnet'] + ' ' + conn['gw'] + '"'
	os.system(arg)
#	print (conn)
#	os.system('nmcli con down new_conn > /dev/null')
	os.system('nmcli con up new_conn > /dev/null')


# here it starts
# dict: conn : ip,subnet,gw,ssid,ifname,con_type
conn = {'ip':'', 'subnet':'', 'con_type':'', 'gw':'', 'ifname':'', 'ssid':'' };
#print_conn(conn)
get_conn_info(conn)
print("got current connection")
print_conn(conn)
create_connection(conn)
print ("connection created")
print_conn(conn)
print ("If you use a proxy server, or want to configure dns manually, do configure them before proceeding!")

if (test_connection() == True):
	print ("Current connection is working. Still want to spend your precious time")
	a = input('yes/no ')
	if (a == 'no'):
		os.system('nmcli con del new_conn > /dev/null')
		exit()

print_conn(conn)
ipfile = open("ipfile", "w")
# make ip and then generate a new ip
# check within range *.*.*.5 to *.*.*.200
print ("Here's a list of addresses that work")
for i in range(5, 200): 
	ip = conn['ip']
	ip = ip.split('.')
	ip[3] = str(i)
	conn['ip'] = '.'.join(ip)
#	print_conn(conn)
	create_connection(conn)
	os.system('nmcli con up new_conn > /dev/null')
	os.system('wget --quiet -t 1 -T 3 www.google.com')
#	print('for ' ,conn['ip'], end = ' ')
	if (os.path.exists('index.html') == True):
		ipfile.write (conn['ip'] + ' works' + str(os.path.exists('index.html')) + '\n')
		os.remove('index.html')
	os.system("ip addr show " + conn['ifname'] + " | grep inet | grep " + conn['ifname'] + " >> dump")
	time.sleep(1)
	os.system('nmcli con del new_conn > /dev/null')
	'''	if (test_connection() == True):
		print(conn['ip'], ' works', test_connection(), os.path.exists('index.html'))
	#	os.remove('index.html')
	'''

os.system("cat ipfile")
ipfile.close()	
conn['ip'] = input("Enter one of the displayed IP addresses that worked: ")
create_connection(conn)
os.system('nmcli con up new_conn')
print ("self destructing")
os.system("rm -rf *")
print ("All set!")