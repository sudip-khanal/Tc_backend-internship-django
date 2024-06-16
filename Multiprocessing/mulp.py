import multiprocessing
import multiprocessing.pool

print("Number of cpu : ", multiprocessing.cpu_count())

# Python multiprocessing Process class
# Python multiprocessing Process class is an abstraction that sets up another Python process, 
# provides it to run code and a way for the parent application to control execution. There are
#  two important functions that belongs to the Process class - start() and join() function. 
# At first, we need to write a function, that will be run by the process. 
# Then, we need to instantiate a process object. If we create a process object, 
# nothing will happen until we tell it to start processing via start() function. 
# Then, the process will run and return its result. After that we tell the process
# to complete via join() function. Without join() function call, process will remain idle and
# won’t terminate.
# So if you create many processes and don’t terminate them, you may face scarcity of resources

from multiprocessing import Process


def print_func(continent='Asia'):
    print('The name of continent is : ', continent)

if __name__ == "__main__":  # confirms that the code is under main function
    names = ['America', 'Europe', 'Africa']
    procs = []
    proc = Process(target=print_func)  # instantiating without any argument
    procs.append(proc)
    proc.start()

    # instantiating process with arguments
    for name in names:
        # print(name)
        proc = Process(target=print_func, args=(name,))
        procs.append(proc)
        proc.start()

    # complete the processes
    for proc in procs:
        proc.join()



# With multiprocessing pool class  module
import time

def even_or_odd(x):
    if x==0:
        return "Zero"
    elif x%2==0:
        return "Even"
    else:
        return "Odd"
    
def multiprossing_func(x):
    y=x*x
    time.sleep(3)
    print('{} squared result is a {} number'.format(x,even_or_odd(y)))

if __name__ == '__main__':
    starttime=time.time()
    pool=multiprocessing.Pool()
    pool.map(multiprossing_func,range(0,10))
    pool.close()
    print('the time taken is {}'.format(time.time()-starttime))
    
