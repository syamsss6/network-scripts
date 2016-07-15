from socket import *

TO_ADDR = ('127.0.0.1', 8010)
MSG_LEN=1000
fd = socket(AF_INET, SOCK_DGRAM)

while True:
 msg = raw_input('CLIENT:')
 fd.sendto(msg, TO_ADDR)
 data,address=fd.recvfrom(MSG_LEN)
 print data


