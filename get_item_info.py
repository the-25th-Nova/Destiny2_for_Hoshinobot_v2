import pickle, os, requests
import hoshino
from bs4 import BeautifulSoup
#get the resource
d = hoshino.config.RES_DIR + 'img/destiny2/'
with open(f'{d}mani_en.pickle','rb') as raw:
	en_data = pickle.load(raw)
with open(f'{d}mani_zh.pickle','rb') as raw:
	zh_data = pickle.load(raw)

def get_hash(name=''):
	hash = 0
	for i in en_data['DestinyInventoryItemDefinition']:
		try:
			a = en_data['DestinyInventoryItemDefinition'][i]['displayProperties']['name']
		except:
			a = '0'
		if name.lower() == a.lower():
			hash = i
	for i in zh_data['DestinyInventoryItemDefinition']:
		try:
			a = zh_data['DestinyInventoryItemDefinition'][i]['displayProperties']['name']
		except:
			a = '0'
		if name == a:
			hash = i
	return hash
			
def get_item(name):
	i = get_hash(name)
	info = {'hash':i}
	try:
		a = zh_data['DestinyInventoryItemDefinition'][i]['displayProperties']['name']
	except:
		a = []
	if a:
		for n in zh_data['DestinyInventoryItemDefinition'][i]['displayProperties']:
			info[n] = zh_data['DestinyInventoryItemDefinition'][i]['displayProperties'][n]
		base_url = 'https://www.bungie.net'
		info['icon'] = base_url + info['icon']
		get_icon(info['hash'],info['icon'])
		return info
	else:
		return {}
		
def get_icon(hash,url):
	headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36 LBBROWSER'}
	miss_url = 'https://www.bungie.net/img/misc/missing_icon_d2.png'
	try:
		with requests.get(url,headers=headers) as img:
			if is_icon(img):
				#print(img.content)
				if not os.path.isfile(f'{d}{hash}.jpg'):
					open(f'{d}{hash}.jpg','wb').write(img.content)
			else:
				with requests.get(miss_url,headers=headers) as img:
					open(f'{d}{hash}.jpg','wb').write(img.content)
	except:
		with requests.get(miss_url,headers=headers) as img:
			open(f'{d}{hash}.jpg','wb').write(img.content)
			
def is_icon(r):
	tit = BeautifulSoup(r.text, 'lxml').find_all('h1')
	if tit:
		return False
	else:
		return True
'''
def get_icon_url(info):
	headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36 LBBROWSER'}
	base_url = 'https://www.bungie.net'
	miss_url = 'https://www.bungie.net/img/misc/missing_icon_d2.png'
	if info:
		print('有了')
		if info['hasIcon']:
			icon_url = base_url + info['icon']
			return icon_url
		
	else:
		return miss_url
'''
#print(get_item('遗言'))
#get_icon('https://www.bungie.net/common/heiger.jpg')
