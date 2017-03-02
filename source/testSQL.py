import asyncio
import logging;logging.basicConfig(level=logging.INFO)
from source import orm
from source.Model import User

async def test():
    await orm.create_pool(loop=loop, host='127.0.0.1', port=3306, user='root', password='123456', db='awesome')
    u = User(name='xiaopeng', email='chenhao8@qq.com', passwd='1234567890', image='about:blank')
    await u.save()
    u = User(name='xiaopeng23', email='chenhao8@23qq.com', passwd='123456789230', image='about:bla23nk')
    await u.save()
    logging.info('tesk ok')

loop = asyncio.get_event_loop()
loop.run_until_complete(test())

loop.close()