import time
import grequests
import aiohttp
import asyncio
import json


async def start_benchmark_aiohttp(urls: list, json_post: dict):
    result = []
    
    async with aiohttp.ClientSession() as session:
        tasks = [session.post(url=url, json=json_post) for url in urls]
        responses = await asyncio.gather(*tasks)
        
        for response in responses:
            result.append(await response.json(content_type='text/html'))
        return result
    

def start_benchmark_grequests(urls: list, json_post: dict) -> list:
    batch_requests = [grequests.post(url=url, json=json_post) for url in urls]
    responses = grequests.map(batch_requests)

    return [json.loads(response.text) for response in responses]


if __name__ == '__main__':
    test_api = ["https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search" for _ in range(30)]
    json_post = {
        'page': 1,
        'rows': 1,
        'asset': 'USDT',
        'fiat': 'UAH',
        'tradeType': 'BUY'
    }
    start = time.time()
    start_benchmark_grequests(test_api, json_post)
    time_grequests = time.time() - start
    
    start = time.time()
    asyncio.run(start_benchmark_aiohttp(test_api, json_post))
    time_aiohttp = time.time() - start
    
    print(f'\ngrequests - {time_grequests}\naiohttp - {time_aiohttp}')
