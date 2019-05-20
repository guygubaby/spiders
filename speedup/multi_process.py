import multiprocessing as mp
import time


def test_func(name):
    print(f'start {name}')
    time.sleep(2)
    print(f'end {name}')


if __name__ == '__main__':
    pool=mp.Pool(mp.cpu_count())
    for i in range(4):
        pool.apply_async(test_func,('guygubaby',))
    pool.close()
    pool.join()