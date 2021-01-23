'''def militarytime(time):
	timeperiod=time[-2:]
	if(timeperiod=='PM'):
		hrs=time[:2]
		if(hrs=='12'):
			time=time.replace('PM','')
			return time
		else:
			time=time.replace('PM','')
			time=time.replace(time[:2],str(int(hrs)+12),1)
			
			return time
	elif(timeperiod=='AM'):
		hrs=time[:2]
		if(hrs=='12'):
			time=time.replace(hrs,'00',1)
			return time
		else:
			time=time.replace(time[:2],str(int(hrs)+12),1)
			time=time.replace(timeperiod,'AM',1)
			return time'''
def militarytime(time):
	tp=time[-2:]
	if(tp=='AM'):
		hours=time[:2]
		if(hours=='12'):
			time=time.replace('12','00',1)
			return time[:-2]
		else:
			return time[:-2]
	elif(tp=='PM'):
		hours=time[:2]
		if(hours=='12'):
			return time[:-2]
		else:
			time=time.replace(hours,str(int(hours)+12),1)
			return time[:-2]
		
		
