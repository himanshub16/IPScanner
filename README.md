 ironport-jugaad  
 Author : Himanshu Shekhar < https://github.com/himanshushekharb16/ironport-jugaad/
 -------------------
  **********FOR ETHICAL PURPOSES ONLY**********
=================================================================================================================================
Temporary solutions to multiple login on ironport @ IIITA

What is this about ?
---------------------------------------------------------------------------------------------------------------------------------
On newtorks using Cisco Ironport and allowing authentication via proxy, multiple logins by same credentials are prevented, which is an inconvenience in one way, while a safeguard in other way.
This is a tool to exploit one of the loophole of the network, *** for ethical purposes only ***

What is the loophole ?
---------------------------------------------------------------------------------------------------------------------------------
Suppose, a person X does a login on an IP A.B.C.D, the session starts and lasts for a specific time, after which he/she has to login again. However, if you end your browsing session within that time, you session still remains open.
So, someone using the DHCP connecting using the same IP as above can use the network for the time remaining without making a login, but the usage will on some other credential.

What it does?
---------------------------------------------------------------------------------------------------------------------------------
It changes your system IP, and tries several possible combinations of the local network, downloading a simple file. If a session is active on the IP, the download will be successful, else, HTTP 503 Forbidden access. That's all.

Purpose of this hack!
---------------------------------------------------------------------------------------------------------------------------------
Ethical hacking is done to cause improvements in network. Also, this would serve as a tool for usage in critical times.
