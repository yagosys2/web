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

async def main():
    loop = asyncio.get_running_loop()

    task = [
    ask_sleep("A", 2),
    ask_sleep("B", 6)
    ]
    await asyncio.wait(task)

    await do_other_things()
    await ask_sleep('C',5)

asyncio.run(main())

