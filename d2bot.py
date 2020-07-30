
from nonebot import *
from hoshino import Service
from .findxur import *
from datetime import datetime

sv_help = '[@[bot]老九]查看老九位置'
sv = Service('destiny2_bot', help_=sv_help, bundle='d2bot')

_bot = get_bot()
@sv.on_command('老九',aliases=('Xur','xur'),only_to_me=True)
async def xur(session: CommandSession):
	icon = MessageSegment.image('https://www.bungie.net/common/destiny2_content/icons/801c07dc080b79c7da99ac4f59db1f66.jpg')
	msg = icon + find_xur()
	await session.send(msg)
