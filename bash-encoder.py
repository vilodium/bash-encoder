#!/bin/python3
# |<****>|
# Writen By: ViloDium
# At: 2021-09
# Description: Bash command encoder 
# |<****>|

# IMP0RTS

import os
import base64

# FIRST THINGS FIRST
# C0L0RS
#-----------------
ntext = '\033[0m'
blue = '\033[1;34m'
green = '\033[0;32m'
red = '\033[1;31m'
yellow = '\033[1;33m'
purple = '\033[0;35m'
cyan = '\033[0;36m'
good = '\n' + green + '{+}' + ntext + ' '
bad = '\n' + red + '{-} '
important = '\n' + yellow + '{*} '
error = '\n\n' + '\033[1;31;42m {X} '
#-----------------
shell = '<*-}> '

# INF0

print(red + "\n*Bash-encoder*")
print(ntext + "Encodes bash commands into base64 encoding")

# MAIN 

try:
    encodable = input(important + 'Enter command to encode:\n' + shell)
    encodedBytes = base64.b64encode(encodable.encode("utf-8"))
    encoded = str(encodedBytes, "utf-8")
except:
	print(error + "AN ERROR ACCURED")
	exit()

encoded_command = "echo '" + encoded + "' | base64 -d | bash"


print(red + "\nThis is your encoded command: " + ntext + encoded_command + green + "\nUse it carefuly\n")
