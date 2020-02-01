# Permission denied error : sudo chmod a+rw /dev/ttyACM0

import serial
import sys
sys.path.insert(0,"/usr/local/lib/python2.7/dist-packages")
import pymysql
#from time import localtime, strftime
from time import gmtime, strftime
import datetime
T = serial.Serial('/dev/ttyACM1', 9600, timeout=1) 
#db = MySQLdb.connect(host='localhost', user='root', passwd='', db='nas')
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='nas', charset='utf8')
curs = db.cursor(pymysql.cursors.DictCursor)
sql = "insert into sensor_data(time,vibration_c,vibration_s, noise) values (now(), %s, %s, %s)"
now = datetime.datetime.now()
if db.open:
    print("connected")

while True:
    
	thing = T.readline()
	#print(thing)
	try:
		(temp_a, data_list, temp_b) = thing.decode('utf-8').split('^',3)
		try:
			noise , viberator_s,viberator_c = data_list.split(',',3)
			print(float(noise))
			print(float(viberator_s))
			print(float(viberator_c))   
			if float(viberator_c) > 20 and float(viberator_s) > 20:                  
				curs.execute(sql, (float(viberator_c), float(viberator_s),float(noise)))
				db.commit()           
		except:
			pass
	except:
		pass
	#print(data_list)
	 
	

''' 
def timeAverage():

	temp = T.readline()
	temp = temp[:-2]
	temp = eval(temp)
	Temp = temp[1]

	N = 10
	p = 0

	while (p < N - 1):
		temp = T.readline()
		temp = temp[:-2]
		temp = eval(temp)

		Temp = Temp + temp[1]
		p = p + 1

	time = strftime("%Y-%m-%d %H:%M:%S", localtime())
	Temp = Temp / float(N)

	return (time, Temp)


while True:

	data = timeAverage()
	fTime = data[0]
	fTemp = "%.1f\n" % data[1]
	print(fTemp)
db = MySQLdb.connect(host='localhost', user='root', passwd='', db='nas')

	with db:
		cur = db.cursor()

	cur.execute("INSERT INTO SENSOR_DATA(time,vibration_c, vibration_s, noise) VALUES (%f, %f, %f)", (fTime, fTemp, ))
	db.commit()
'''
