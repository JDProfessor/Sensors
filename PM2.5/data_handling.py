#!/usr/bin/python
# coding:utf-8

import serial

#'\xaa\x00\x0c\x00Wc\xff'

def searchEnd():
	for i in range(7):
		string = get_string.read()
		if string == '\xff':
			break

def get_check_num(Byte,checkNum):
	for i in range(1,5):
		checkNum = ord(Byte[i]) + checkNum
	return checkNum

def countPm2_5(checkNum,Byte):
	if checkNum == ord(Byte[5]):
		vout = (float(ord(Byte[1]))*256 + float(ord(Byte[2])))/1024*5   	#	print 'vout:%s' %vout
		return vout*550

def show(pm2_5):
	if pm2_5 <=50:
		print '空气质量：优'
	elif pm2_5 <=100:
		print '空气质量：良'
	elif pm2_5 <=150:
		print '空气质量：轻度污染'
	elif pm2_5 <=200:
		print '空气质量：中度污染'
	elif pm2_5 <=300:
		print '空气质量：重度污染'
	elif pm2_5 <=500 :
		print '空气质量：严重污染'
	else :
		print '爆表'

if __name__ == '__main__':

	while 1:
		checkNum = 0
		get_string = serial.Serial('/dev/ttyAMA0',2400)
		searchEnd()
		Byte = get_string.read(7)

		if Byte[0] == '\xaa':
			print 'OK'
			checkNum = get_check_num(Byte,checkNum)
			pm2_5 = countPm2_5(checkNum,Byte)
			print'PM2.5测量值： %s'%(pm2_5)
			show(pm2_5)

		else :
			print 'The first byte is wrong'
			continue	
