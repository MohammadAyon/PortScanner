#!/bin/python3

import sys
import socket
from datetime import datetime
#we have to define our targer 
if len(sys.argv)==2:
	target=socket.gethostbyname(sys.argv[1])
else:
	print("Inavlid amount of arguments.")
	print("Syntax :python3 scanner.py <ip>")
	
print("-"*50)
print("Scanning target "+target)
print("Time started :" +str(datetime.now()))
print("-"*50)		

try:
	for port in range(50,85):
		s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result=s.connect_ex((target,port))#return error
		if result==0:
			print("Port {} is open ".format(port))

except KeyboardInterrupt:
	print("\n Exiting program.")
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved .")

	
	
		
