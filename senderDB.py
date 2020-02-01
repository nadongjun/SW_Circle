# Permission denied error : sudo chmod a+rw /dev/ttyACM0

import serial
import sys
sys.path.insert(0,"/usr/local/lib/python2.7/dist-packages")
import pymysql
#from time import localtime, strftime

T = serial.Serial('/dev/ttyACM0', 9600, timeout=1) 
#db = MySQLdb.connect(host='localhost', user='root', passwd='', db='nas')
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='nas', charset='utf8')

curs = conn.cursor(pymysql.cursors.DictCursor)

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
            sql = """insert into sensor_data(time,viberator_c,viberator_s, noise) values (now(), %f, %f, %f)"""
            curs.execute(sql, (viberator_c, viberator_s, noise))
            conn.commit()      
            
            
		except:
			pass
	except:
		pass
