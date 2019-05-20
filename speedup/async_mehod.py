import asyncio


async def test(t):
    print(f'{t} start ...')
    await asyncio.sleep(t)
    print(f'{t} end ...')


async def main(loop):
    tasks=[
        loop.create_task(test(t)) for t in range(5)
    ]
    await asyncio.wait(tasks)


if __name__ == '__main__':
    loop=asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    loop.close()
