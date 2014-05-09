import smtplib
import socket

#returns 1 if connected to the internet, else -1
def waitForConn():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		sock.connect(("www.google.com", 80))
		return 1;
	except:
		print("not connected...")
		return -1;


#sends a text to your cell phone telling you that you are connected
def confirmConn():
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login('email', 'password')
	server.sendmail('brent', 'phonenumber@mms.att.net', 'you are connected.')

connected = -1
#while not connected, try to connect
while connected == -1:
	connected = waitForConn()

#connection made, send text
confirmConn()
