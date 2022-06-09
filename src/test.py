# -*- coding: UTF-8 -*- 
import redis
import aioredis
import asyncio
import aiohttp


async def main():
    r = await aioredis.from_url("redis://192.168.150.128", db=0) 
    #print(await r.keys())
    temp = 5
    #print(f'the answer is {temp}')
    print('the answer is {}'.format(temp))

    #print(await r.ping())


if __name__ == '__main__': 
    asyncio.run(main()) 
