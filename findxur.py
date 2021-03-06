#if Xur was not arrive, it will return the time
'''
import requests
a = open('website.txt', 'w')
site = requests.get('https://xur.wiki')
a.write(site.text)
print('Done!')
'''
#import datetime 
from datetime import*
import calendar, math
import requests
from bs4 import BeautifulSoup

headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36 LBBROWSER'}
def get_soup():
	url = 'https://xur.wiki/'
	req = requests.get(url, headers=headers)
	soup = BeautifulSoup(req.text, 'lxml')
	return soup
	
def get_xur_item():
	soup = get_soup()
	xml = soup.find_all('h6', class_='hero_item_name')
	item = []
	for i in xml:
		item.append(i.string)
	return item

def get_xur_pos():
	soup = get_soup()
	item = []
	xml = soup.find_all('h1', class_='location_name')
	#print(xml)
	item.append(xml[0].text)
	xml = soup.find('p', class_='location-text-here').contents[0].text
	item.append(xml)
	xml = soup.find_all('div', class_='location-map lazyload')
	item.append(xml[0].get('data-src'))
	return item

#老九时间

def find_xur():
	if is_xur_arrived():
		#print('Xur was arrived')
		msg = '老九已经到了'
		item = get_xur_pos()
		for i in item:
			msg += f'\n{i}'
	else:
		#print('Xur is not here')
		time = xur_dis()
		msg = '老九去了二次元\n还有' + time + '才能回来'
	return msg

def is_xur_arrived():
	today = datetime.today().weekday()
	#6 0 1 2 3 4 5
	xur_days = [0,1,6]
	#if today == (5 or 6 or 0 or 1 or 3):
	if today in xur_days:
		return True
	elif today == 2:
		if datetime.now().hour >= 1:
			return False
		else:
			return True
	elif today == 5:
		if datetime.now().hour >= 1:
			return True
		else:
			return False
	else:
		return False
	
def xur_dis():
    #print(str(date1 - date2))
    day_n = datetime.today()
    day_x = get_xurTime()
    times = str(day_x - day_n).split(':')
    #print(times)
    daytime = times[0].split('day,')
    if len(daytime) == 1:
        dnh = ' 0天'+times[0]+'时'
    else:
        dnh =  daytime[0].strip()+'天'+daytime[1].strip()+'时'
    #print(dnh)
    sec = str(math.floor(float(times[2])))
    #print(sec)
    difftime = dnh+times[1]+'分'+sec+'秒'
    #print('diff:' + difftime)
    return difftime
    
    
    
def get_xurTime():
    today = datetime.today()
    print(today)
    oneday = timedelta(days = 1)
    today += timedelta(hours = 1-today.hour, minutes = 0-today.minute, seconds = 0-today.second)
    #print(today)
    m6 = calendar.SATURDAY
    while today.weekday() != m6:
        today += oneday
    nextXur = today.strftime('%Y-%m-%d')
    #print(today)
    return today

#print(get_xurTime())
#print(find_xur())
#print(is_xur_arrived())
