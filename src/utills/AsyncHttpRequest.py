# -*- coding: utf-8 -*-
import json
import logging
import asyncio
from datetime import datetime

import aiohttp


logger = logging.getLogger()
async def getQuery(url):
    
    startTime = int(datetime.now().timestamp() * 1000)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            responseCode = resp.status
            contentType  = resp.content_type
        
            if str(responseCode)[0] == "2":
                if contentType.lower() == 'application/json'.lower():
                    json_body = await resp.json()
                elif contentType.lower() == 'text/plain'.lower():
                    content = await resp.text()
                    logger.debug(content)
                    json_body = json.loads(content)
            
                logger.debug(f'content-type: [{contentType}], content: \n{json.dumps(json_body,indent=4)}')
    
    endTime = int(datetime.now().timestamp() * 1000)
    logger.info("Finish Query [%s], cost %d ms, response.status [%d]" % (url, (endTime-startTime), resp.status))
    return json_body

async def postQuery(userId = None, password = None, data = {}, header={}, uri = None):
    if not uri:
        logger.debug("empty uri, return")
        return None

    theAuth = None
    if userId:
        theAuth = aiohttp.BasicAuth(userId, password)

    startTime = int(datetime.now().timestamp() * 1000)
    
    headers = header
    json_body = None

    async with aiohttp.ClientSession(headers=headers, auth=theAuth) as session:
        async with session.post(uri,json=data) as resp:
            responseCode = resp.status
            contentType  = resp.content_type

            if str(responseCode)[0] == "2":
                if contentType.lower() == 'application/json'.lower():
                    json_body = await resp.json()
                elif contentType.lower() == 'text/plain'.lower():
                    content = await resp.text()
                    json_body = json.loads(content)

                logger.debug(f'content-type: [{contentType}], content: \n{json.dumps(json_body,indent=4)}')
                        
    endTime = int(datetime.now().timestamp() * 1000)
    logger.info("Finish Query [%s], cost %d ms, response.status [%d]" % (uri, (endTime-startTime), resp.status))
    return json_body


async def main():
    result = await getQuery()
    print(json.dumps(result, indent=4))

if __name__ == '__main__':
    asyncio.run(main())
