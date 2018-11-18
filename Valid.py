#!/usr/bin/python3

# NES filesize checker, gutted from 6502d
# Doug Fraker 2017-2018

# Permission is hereby granted, free of charge, to any person obtaining a copy of 
# this software and associated documentation files (the "Software"), to deal in the 
# Software without restriction, including without limitation the rights to use, copy, 
# modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, 
# and to permit persons to whom the Software is furnished to do so, subject to the 
# following conditions:
#
# The above copyright notice and this permission notice shall be included in all 
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A 
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT 
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF  
# CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE 
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import sys
import os



if len(sys.argv) < 2:
	print("usage: " + sys.argv[0] + " <path>")
	exit()
path = sys.argv[1]


# initialize some variables

count = 0





# START OF PROGRAM

filename = os.path.basename(path)

try:
	fileIn = open(path, "rb") #read bytes
except:
	print("\nERROR: couldn't find file\n")
	raise
	
print (filename)
filesize = os.path.getsize(path)
print("filesize = ", filesize)
folder = os.path.dirname(path)
	
workArray = fileIn.read() #make a big int array 

testarray = bytearray(b'\x4e\x45\x53\x1a') # NES 1a



# validate header	
	
for i in range (0,4):
	if (workArray[i] != testarray[i]):
		print("\nERROR: couldn't find iNES header\n")
		exit()
		
		
# get ROM sizes
	
prgROM = workArray[4]
prgROMtotal = prgROM * 0x4000
print ("PRGROM size = ", prgROM, " = ", prgROMtotal)

if (prgROM != 0) and (prgROM != 1) and (prgROM != 2) and (prgROM != 4) and (prgROM != 8) and (prgROM != 16) and (prgROM != 32) and (prgROM != 64):
	print ("  PRGROM banks should be a power of 2")
if (prgROM == 0):
	print ("  PRGROM banks can't be zero")

chrROM = workArray[5]
chrROMtotal = chrROM * 0x2000
print ("CHRROM size = ", chrROM, " = ", chrROMtotal)	

if (chrROM != 0) and (chrROM != 1) and (chrROM != 2) and (chrROM != 4) and (chrROM != 8) and (chrROM != 16) and (chrROM != 32):
	print ("  CHRROM banks should be a power of 2")
	
a = 16 + prgROMtotal + chrROMtotal
print ("Header + PRGROM + CHRROM = ", a)
if (filesize != a):		
	print ("ERROR: filesize does not match the header")
	#exit()
else:
	print ("filesize matches header, ok")
	
	
# get mapper	

a = 0
b = 0
c = 0
byte6 = 0
byte7 = 0

byte6 = workArray[6]
a = byte6 >> 4
byte7 = workArray[7]
b = byte7 & 0xf0
c = a + b

Map = ""



if c == 0:
	Map = "NROM"
elif c == 1:
	Map = "MMC1 SxROM"
elif c == 2:
	Map = "UxROM"
elif c == 3:
	Map = "CNROM"
elif c == 4:
	Map = "MMC3 TxROM"	
elif c == 5:
	Map = "MMC5 ExROM"
elif c == 7:
	Map = "AxROM"
elif c == 9:
	Map = "MMC2 PxROM"
elif c == 10:
	Map = "MMC4 FxROM"
elif c == 11:
	Map = "COLOR DREAMS"
elif c == 13:
	Map = "CPROM"
elif c == 16:
	Map = "Bandai"
elif c == 18:
	Map = "Jaleco"
elif c == 19:
	Map = "Namco 163"
elif c == 20:
	Map = "FDS"
elif c == 21:
	Map = "Konami VRC4"
elif c == 22:
	Map = "Konami VRC2"	
elif c == 23:
	Map = "Konami variation"
elif c == 24:
	Map = "Konami VRC6"
elif c == 25:
	Map = "Konami variation"
elif c == 26:
	Map = "Konami VRC6"
elif c == 28:
	Map = "Action 53"
elif c == 30:
	Map = "UNROM 512k, Oversized Homebrew"
elif c == 31:
	Map = "NSF music"
elif c == 32:
	Map = "Irem's G-101"
elif c == 33:
	Map = "Taito's TC0190"
elif c == 34:
	Map = "BNROM or NINA-001"
elif c == 36:
	Map = "TXC"
elif c == 48:
	Map = "Taito's TC0690"
elif c == 64:
	Map = "Tengen RAMBO-1"
elif c == 65:
	Map = "Irem's H3001"
elif c == 66:
	Map = "GxROM or MHROM"
elif c == 67:
	Map = "Sunsoft-3"
elif c == 68:
	Map = "Sunsoft-4"
elif c == 69:
	Map = "Sunsoft FME-7"
elif c == 70:
	Map = "Bandai"
elif c == 71:
	Map = "Codemasters"
elif c == 72:
	Map = "Jaleco's JF-17"
elif c == 73:
	Map = "Konami VRC3"
elif c == 74:
	Map = "Eastern games"
elif c == 75:
	Map = "Konami VRC1"
elif c == 76:
	Map = "Namcot 108"
elif c == 77:
	Map = "Irem"
elif c == 78:
	Map = "Irem"
elif c == 79:
	Map = "NINA-03 or NINA-06"
elif c == 80:
	Map = "Taito's X1-005"	
elif c == 82:
	Map = "Taito's X1-017"	
elif c == 85:
	Map = "Konami VRC7"	
elif c == 86:
	Map = "Jaleco's JF-13"	
elif c == 87:
	Map = "Jaleco"	
elif c == 88:
	Map = "Namco"		
elif c == 89:
	Map = "Sunsoft"	
elif c == 93:
	Map = "Sunsoft"	
elif c == 94:
	Map = "HVC-UN1ROM"	
elif c == 99:
	Map = "Vs. System"	
elif c == 118:
	Map = "TKSROM and TLSROM"	
elif c == 119:
	Map = "TQROM"		
	
else:
	Map = "Other / Too Lazy to type them all in."


print ("Mapper number = ", c, " = ", Map)	


# mirroring = low bit of byte6

a = byte6 & 0x08 # 4 screen
if (a == 0):
	a = byte6 & 0x01 # 2 screen
	
if (a == 0):
	print ("horizontal mirroring")
elif (a == 1):
	print ("vertical mirroring")
else:
	print ("4 screen mode")
	
	
# extra RAM at 6000 = byte6 ? bit 2

a = byte6 & 0x02
if (a != 0):
	print ("extra RAM at $6000, yes")
	
	

fileIn.close					

