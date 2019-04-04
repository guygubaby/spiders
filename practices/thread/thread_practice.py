import threading,time

rlock=threading.RLock()


def run_task(n):
    rlock.acquire()
    with open('test.txt','a+') as f:
        f.write(f'this is thread {n} \n')
    rlock.release()


class MyThread(threading.Thread):
    def __init__(self,id):
        super(MyThread, self).__init__()
        self.id=id

    def run(self):
        run_task(self.id)
        print(f'thread {self.id}')


if __name__ == '__main__':
    start_time=time.time()
    print(f'start time is : {start_time}')
    for i in range(30):
        my_thread=MyThread(i)
        my_thread.start()
        # my_thread.join() # ensure the main thread last quit
    end_time=time.time()
    print(f'end time is : {end_time}')
    print(f'finished with {end_time-start_time}')