
import serial
from time import localtime, strftime

T = serial.Serial('/dev/ttyACM0', 9600, timeout=1) 
 
while True:
 
	thing = T.readline()
	print(thing)
   
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
db = MySQLdb.connect(host='localhost', user='DB 계정이름', passwd='비밀번호', db='DB 이름')

	with db:
		cur = db.cursor()

	cur.execute("INSERT INTO time_temperature(time,temp) VALUES (%s, %s)", (fTime, fTemp))
	db.commit()
'''
