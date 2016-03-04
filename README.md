# IPScanner
A network vulnerability scanner
--------------------------------------------------
In case of environments, where there are a bunch of computers on local network and all connections are recognised using IP address, this tool can give list of all IP address within a specific range where a browsing session was running and has been temporarily suspended or just closed.

One such case is a campus network, where users need to login to use the network, and logins are made with sessions initiated on a particular IP address. 
This tool is supposed to change the system IP address, by creating a new network connection using any interface (Ethernet/Wireless), and check whether network connectivity is there or not.
The readme may not be much clear. So, go forward and try the tool.
This tool currently works on Linux with network-manager "nmcli".
# Do fork the project, especially if you want to make a version for Windows or Mac.

# About files
main.py : This is the main python script.

get_ifaces.bash : This shell script returns the list of interfaces available on the system.

dump : This file contains the logs of current IP address of the system.

ip_file : This file contains the output (result) of whatever scan has been done.

