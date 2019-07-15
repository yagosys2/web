import asyncio  
import time  
from datetime import datetime

async def custom_sleep(name,n):  
    print(f'{name} SLEEP now {datetime.now()}n for {n} seconds')
    await asyncio.sleep(n)
    print(f'{name} end of sleep')

async def  ask_sleep(name, number):  
        print(f'call {name} to sleep {number} seconds')
        await custom_sleep(name,number)
        print(f'wake at {datetime.now()}n')

async def do_other_things():
    print('doing other things')
    await custom_sleep('D',1)

loop = asyncio.get_event_loop()
tasks = asyncio.gather(*[  
    loop.create_task(ask_sleep("A", 2)),
    loop.create_task(ask_sleep("B", 6)),
])

#loop.run_until_complete(asyncio.wait(tasks)) ## finishi all the task in the loop,  
#loop.run_until_complete(asyncio.gather(*tasks))
loop.run_until_complete(tasks)

loop.create_task(do_other_things()) ## put do_other_things into loop for execute whenever resource available 
loop.run_until_complete(custom_sleep('C',7))  ##create new loop and add task custom_sleep  into loop and run loop until compelte

loop.close()


