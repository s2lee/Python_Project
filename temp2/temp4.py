import asyncio
import time
from time import perf_counter

import aiohttp
import requests


def order():
    stime = perf_counter()
    print(time.strftime("%Y-%m-%d %H:%M:%S"))
    cook("pizza")
    print(f"cook pizza elapsed time: {perf_counter() - stime:.2f} seconds")

    stime = perf_counter()
    print(time.strftime("%Y-%m-%d %H:%M:%S"))
    cook("soup")
    print(f"cook soup elapsed time: {perf_counter() - stime:.2f} seconds")

    # stime = perf_counter()
    # print(time.strftime("%Y-%m-%d %H:%M:%S"))
    # asyncio.run(async_cook("pizza"))
    # print(f"cook pizza elapsed time: {perf_counter() - stime:.2f} seconds")

    # stime = perf_counter()
    # print(time.strftime("%Y-%m-%d %H:%M:%S"))
    # asyncio.run(async_cook("soup"))
    # print(f"cook soup elapsed time: {perf_counter() - stime:.2f} seconds")
    print("--------------")

    stime = perf_counter()
    print(time.strftime("%Y-%m-%d %H:%M:%S"))
    asyncio.run(async_cook3("pizza"))
    print(f"cook pizza elapsed time: {perf_counter() - stime:.2f} seconds")

    stime = perf_counter()
    print(time.strftime("%Y-%m-%d %H:%M:%S"))
    asyncio.run(async_cook3("soup"))
    print(f"cook soup elapsed time: {perf_counter() - stime:.2f} seconds")


def cook(menu: str):
    print(menu)
    response_list = []
    for _ in range(15):
        url = "https://reqres.in/api/users"
        response = requests.get(url)
        res_json = response.json()
        response_list.append(res_json["data"])


async def async_cook(menu: str):
    print(menu)
    response_list = []
    for _ in range(10):
        url = "https://reqres.in/api/users"
        response = requests.get(url)
        res_json = response.json()
        response_list.append(res_json["data"])


async def async_cook2(domain: str, data: dict):
    try:
        async with aiohttp.ClientSession() as session:
            url = "https://reqres.in/api/users=2"
            async with session.get(url) as response:
                return await response.text()
    except Exception as e:
        print(e)


async def async_cook3(menu: str):
    coro_list = [async_cook2("domain", {"shop_id": "d"}) for _ in range(15)]
    await asyncio.gather(*coro_list)


stime = perf_counter()
order()
print(f"order elapsed time: {perf_counter() - stime:.2f} seconds")

