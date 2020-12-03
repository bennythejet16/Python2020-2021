#!/usr/bin/env python3
#bk,cwc 12-3-20

def dec2bin(dec):
	binValue = bin(dec)
	binS = str(bin(dec))
	b = binS.replace('0b','')
	print(dec,binvalue,b) #debug
	return b
	
def main():
		print("* Deciaml to Binary * * * * * *")
		binString = dec2bin(10)
		print(10,binString)
		binString = dec2bin(245)
		print(245,binString)
		
main()
