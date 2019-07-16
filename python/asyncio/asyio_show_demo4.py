#https://cheat.readthedocs.io/en/latest/python/asyncio.html
import asyncio  
import time  
from datetime import datetime

async def custom_sleep(name,n):### 这是一个协程函数   
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

async def my_call_back():
    print('i am finished')

async def main():
    loop = asyncio.get_running_loop() ###取得当前的event loop

    task = [
    ask_sleep("A", 2), ###运行该任务, 在该任务block时交回控制权，执行下一个任务，等待回调
    ask_sleep("B", 6) ###运行该任务，在该任务block时交回控制权。等待回调
    ]
    await asyncio.wait(task)  ###将任务加入event loop,有资源就运行，直到运行完毕。执行下一行.asyncio.wait是运行一组任务,功能类似
    ###与asyncio.gather, gather更高层一些。
    future = loop.create_task(do_other_things()) ###create_task是将一个协程放入event_loop,有空闲时就执行,这个结果用future对象表示
    #asyncio.ensure_future(do_other_things(),loop=loop)### 这个与create_task的作用相同
    await ask_sleep('C',5) ###暂停当前程序，运行ask_sleep,当其执行到sleep(5)时处于block状态，资源空闲，就去
    ###执行在event_loop里的do_other_things.
    #await do_other_things() ###暂停当前程序，运行do_other_things,直到完成

asyncio.run(main()) ### 创建一个event loop , 并运行协程函数main,返回一个协程对象（类似与生成器）。

