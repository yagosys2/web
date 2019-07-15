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
    loop = asyncio.get_running_loop() ###取得当前的event loop

    task = [
    ask_sleep("A", 2), ###运行该任务, 在该任务block时交回控制权，执行下一个任务，等待回调
    ask_sleep("B", 6) ###运行该任务，在该任务block时交回控制权。等待回调
    ]
    await asyncio.wait(task)  ###将任务加入event loop,有资源就运行，直到运行完毕。执行下一行
    await ask_sleep('C',5) ###暂停当前程序，运行ask_sleep,直到完成 
    await do_other_things() ###暂停当前程序，运行do_other_things,直到完成

asyncio.run(main()) ### 创建一个event loop , 并运行main())

