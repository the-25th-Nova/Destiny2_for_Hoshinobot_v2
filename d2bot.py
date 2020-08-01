import os, hoshino
from nonebot import *
from hoshino import Service, R
from .findxur import *
#from .spider import *
from .get_item_info import *
from datetime import datetime

r_url = hoshino.config.RES_DIR

sv_help = '[@[bot]老九]查看老九位置\n[[@bot]老九历史]查看老九上周售卖物品'
sv = Service('destiny2_bot', help_=sv_help, bundle='d2bot')

icon = MessageSegment.image('https://www.bungie.net/common/destiny2_content/icons/801c07dc080b79c7da99ac4f59db1f66.jpg')#Xur pic

_bot = get_bot()
@sv.on_command('老九',aliases=('Xur','xur'),only_to_me=True)
async def xur(session: CommandSession):
	status = find_xur()
	msg = icon + status
	msg = msg + '\n地图位置请点开上方链接\n'
	await session.send(msg)
	if is_xur_arrived():
	    msg = '老九在卖:\n'
	    for i in get_xur_item():
	    	i = re_item(i)
	    	msg += i + '\n\n'
	    await session.send(msg)
'''
@sv.on_command('老九历史',aliases=('XurHis','xurhis'),only_to_me=True)
async def xurhis(session: CommandSession):
	item, pic = Xur_his()
	msg = icon + '老九上周卖了:\n'
	await session.send(msg)
	for i in range(len(item)):
		it = item[i]
		msg = it
		should_down = False
		if os.path.isfile(f'{r_url}img/destiny2/{it}.jpg'):
			msg = msg + R.img(f'destiny2/{it}.jpg').cqcode
		else:
			should_down = True
		await session.send(msg)
	if should_down:
	    await session.send('阿巴阿巴 图片不存在，正在下载，稍后再试吧！')
	    download(r_url)
'''

@sv.on_command('查询D2',only_to_me=True)
async def search(session: CommandSession):
	text = session.current_arg_text.strip()
	msg = re_item(text)
	await session.send(msg)
'''
@sv.on_command('更新D2资源',aliases=(),only_to_me=True)
async def upres(session: CommandSession):
	await session.send('更新中')
	download(r_url)
	'''
def re_item(text):
	info = get_item(text)
	try:
		hash = info['hash']
		desc = info['description']
		img = R.img(f'destiny2/{hash}.jpg').cqcode
		msg = info['name'] + img + f'\n\n{desc}\n\n更多信息：https://www.bungie.net/zh-cht/Explore/Detail/DestinyInventoryItemDefinition/{hash}'
		return msg
	except:
		return  '查询出错辣，请使用官方简中名称或英文查询呐'
