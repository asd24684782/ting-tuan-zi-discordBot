import asyncio 
import time 

async def dosomething(num): 
    print('start{}'.format(num)) 
    await asyncio.sleep(num) 
    print('sleep{}'.format(num)) 

async def main(): 
    task1 = asyncio.create_task(dosomething(1)) 
    task2 = asyncio.create_task(dosomething(2)) 
    task3 = asyncio.create_task(dosomething(3))
    task4 = asyncio.create_task(dosomething(4))
    task5 = asyncio.create_task(dosomething(5))
    task6 = asyncio.create_task(dosomething(6))
    task7 = asyncio.create_task(dosomething(7))
    task8 = asyncio.create_task(dosomething(8))
    task9 = asyncio.create_task(dosomething(9))
    
    await task1 
    await task2 
    await task3
    await task4
    await task5
    await task6
    await task7
    await task8
    await task9
    tasks = [dosomething(i) for i in range(1, 10)]
    await asyncio.gather(*tasks, return_exceptions=True)
    print(result)

if __name__ == '__main__': 
    time_start = time.time() 
    asyncio.run(main()) 
    print(time.time() - time_start) 
