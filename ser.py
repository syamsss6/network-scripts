from socket import *

LOCAL_ADDR = ('127.0.0.1', 8010)
MSG_LEN = 1000

fd = socket(AF_INET, SOCK_DGRAM)

fd.bind(LOCAL_ADDR)

while True:
 ss,address= fd.recvfrom(MSG_LEN)
 print ss
 msg=raw_input('SERVER:')
 fd.sendto(msg,address) 

